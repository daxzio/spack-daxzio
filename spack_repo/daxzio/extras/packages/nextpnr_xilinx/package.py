# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import tempfile

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


# Representative -1 package per die for common eval-board footprints.
DEVICE_PARTS = {
    "xc7s25": "xc7s25csga324-1",
    "xc7s50": "xc7s50csga324-1",
    "xc7a35t": "xc7a35tcsg324-1",
    "xc7a100t": "xc7a100tcsg324-1",
    "xc7k325t": "xc7k325tffg676-1",
}


def _prjxray_family(device):
    if "xc7s" in device:
        return "spartan7"
    if "xc7k" in device:
        return "kintex7"
    if "xc7z" in device:
        return "zynq7"
    if "xc7v" in device:
        return "virtex7"
    return "artix7"


class NextpnrXilinx(CMakePackage):
    """Place-and-route tool for Xilinx 7-series FPGAs (openXC7 fork).

    Implements the Yosys + nextpnr-xilinx + Project X-Ray open-source flow
    for Spartan-7, Artix-7, Kintex-7, and related 7-series devices.
    """

    homepage = "https://github.com/openXC7/nextpnr-xilinx"
    git = "https://github.com/openXC7/nextpnr-xilinx.git"

    maintainers("davekeeshan")

    license("ISC")

    version("main", branch="main", submodules=True)
    version(
        "0.9.3",
        commit="68aeeb39f92e39bfb239c7e4a44dd93451fc1889",
        submodules=True,
    )

    variant(
        "devices",
        default="xc7s25,xc7s50,xc7a35t,xc7a100t,xc7k325t",
        values=tuple(DEVICE_PARTS.keys()),
        multi=True,
        description="7-series dies to build chip databases for at install time",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.10:", type="build")
    depends_on("git", type="build")
    depends_on("boost+filesystem+thread+program_options+iostreams+python", type=("build", "link"))
    depends_on("eigen", type=("build", "link"))
    depends_on("python@3.9:", type=("build", "link", "run"))
    depends_on("prjxray-db", type=("build", "run"))
    depends_on("prjxray-db@master", when="devices=xc7s25")
    depends_on("prjxray", type="run")

    def patch(self):
        filter_file(
            "set(boost_libs filesystem thread program_options iostreams system)",
            "set(boost_libs filesystem thread program_options iostreams)",
            "CMakeLists.txt",
        )
        filter_file(
            "#include <climits>",
            "#include <climits>\n#include <cstdint>",
            "3rdparty/json11/json11.cpp",
        )

    def cmake_args(self):
        spec = self.spec
        args = [
            "-DARCH=xilinx",
            "-DBUILD_GUI=OFF",
            "-DBUILD_TESTS=OFF",
            "-DUSE_OPENMP=ON",
        ]
        if spec.satisfies("@0.9.3:"):
            args.append("-DCURRENT_GIT_VERSION=68aeeb3")
        return args

    @run_after("install")
    def install_share_and_chipdbs(self):
        spec = self.spec
        prefix = self.prefix
        share = join_path(prefix, "share", "nextpnr")
        mkdirp(share)

        install_tree("xilinx/python", join_path(share, "python"))
        install("xilinx/constids.inc", share)

        meta_src = "xilinx/external/nextpnr-xilinx-meta"
        if os.path.isdir(meta_src):
            install_tree(meta_src, join_path(share, "external", "nextpnr-xilinx-meta"))

        chipdb_dir = join_path(share, "chipdb")
        mkdirp(chipdb_dir)

        # CMake builds bbasm but does not install it (upstream bba/bba.cmake).
        bbasm_path = join_path(prefix.bin, "bbasm")
        install(join_path(self.build_directory, "bbasm"), bbasm_path)
        set_executable(bbasm_path)

        python = spec["python"].command
        bbasm = Executable(bbasm_path)
        bbaexport = join_path(share, "python", "bbaexport.py")
        db_root = spec["prjxray-db"].prefix
        db_root = join_path(db_root, "share", "prjxray-db")
        meta_root = join_path(share, "external", "nextpnr-xilinx-meta")

        selected = spec.variants["devices"].value
        if isinstance(selected, str):
            selected = (selected,)

        with tempfile.TemporaryDirectory() as tmpdir:
            for die in selected:
                part = DEVICE_PARTS[die]
                family = _prjxray_family(part)
                xray_path = join_path(db_root, family)
                meta_path = join_path(meta_root, family)
                bba_path = join_path(tmpdir, f"{die}.bba")
                bin_path = join_path(chipdb_dir, f"{die}.bin")

                python(
                    bbaexport,
                    "--device",
                    part,
                    "--xray",
                    xray_path,
                    "--metadata",
                    meta_path,
                    "--bba",
                    bba_path,
                )
                bbasm("-l", bba_path, bin_path)

    def setup_run_environment(self, env):
        share = join_path(self.prefix, "share", "nextpnr")
        env.prepend_path("PATH", self.prefix.bin)
        env.set("NEXTPNR_XILINX_PYTHON_DIR", join_path(share, "python"))
        env.set("NEXTPNR_XILINX_CHIPDB", join_path(share, "chipdb"))
        env.set("PRJXRAY_DB_DIR", join_path(self.spec["prjxray-db"].prefix, "share", "prjxray-db"))
