# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Prjxray(CMakePackage):
    """Project X-Ray: documentation and tools for Xilinx 7-series bitstreams.

    Installs the C++ bitstream utilities (xc7frames2bit, bitread, xc7patch)
    and Python libraries/scripts needed to convert nextpnr-xilinx FASM output
    into a .bit file. Vivado is not required for this consumer build.
    """

    homepage = "https://github.com/openXC7/prjxray"
    git = "https://github.com/openXC7/prjxray.git"

    maintainers("davekeeshan")

    license("ISC")

    version("master", branch="master", submodules=True)
    version(
        "0.9.2",
        commit="78d98b98dc189a89cd1def61cee7c938f51bc6e5",
        submodules=True,
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.14:", type="build")
    depends_on("git", type="build")
    depends_on("python@3.9:", type="run")
    depends_on("py-fasm", type="run")
    depends_on("py-intervaltree", type="run")
    depends_on("py-pyjson5", type="run")
    depends_on("py-pyyaml", type="run")
    depends_on("py-simplejson", type="run")
    depends_on("py-numpy", type="run")

    def patch(self):
        filter_file("VERSION 3.5.0", "VERSION 3.14.0", "CMakeLists.txt")
        filter_file("VERSION 3.0.2", "VERSION 3.14.0", "third_party/gflags/CMakeLists.txt")
        filter_file("VERSION 2.8.12", "VERSION 3.14.0", "third_party/cctz/CMakeLists.txt")

    def setup_build_environment(self, env):
        env.append_flags(
            "CXXFLAGS",
            "-include stdint.h -Wno-free-nonheap-object -Wno-deprecated",
        )

    @run_after("install")
    def install_python_bits(self):
        py_root = join_path(self.prefix, "share", "prjxray", "python")
        mkdirp(py_root)
        install_tree("prjxray", join_path(py_root, "prjxray"))

        bindir = self.prefix.bin
        mkdirp(bindir)
        for script in ("fasm2frames.py", "bit2fasm.py"):
            src = join_path("utils", script)
            dst_name = script.replace(".py", "")
            install(src, join_path(bindir, dst_name))
            set_executable(join_path(bindir, dst_name))

    def setup_run_environment(self, env):
        py_root = join_path(self.prefix, "share", "prjxray", "python")
        env.prepend_path("PYTHONPATH", py_root)
        env.set("PRJXRAY_PYTHON_DIR", py_root)
        env.set("XRAY_DIR", self.prefix)
