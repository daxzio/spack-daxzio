# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class RiscvOpenocd(AutotoolsPackage):
    """The Open On-Chip Debugger (OpenOCD) aims to provide debugging, in-system
    programming and boundary-scan testing for embedded target devices.
    """

    license("GPL-2.0-or-later")

    homepage = "https://openocd.org/"
    url = "https://github.com/riscv-collab/riscv-openocd/archive/refs/tags/v2018.12.0.tar.gz"
    git = "https://github.com/riscv-collab/riscv-openocd.git"

    maintainers("davekeeshan")

    version("master", branch="master", submodules=True)

    version("2025.06.12", commit="5a39519f39501552e98fa2fe4cbfea2276d55e9f", submodules=True)
    version("2025.03.31", commit="2605cbd73c36998e76d32cded95a02b424870626", submodules=True)
    version("2025.03.02", commit="67082829da364ad042eea12a455450d707ea4d57", submodules=True)
    version("2025.01.29", commit="5de7310881c18a50797e8d96cf6d3f3aeb2aa4d0", submodules=True)
    version("2024.11.21", commit="1bf7efb2d5be792116bad3d0d7cfb812228d18ea", submodules=True)
    version("2018.12.0", commit="c3c76bfafa6612dc56b3914c9f93eb2a790ef87b", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    variant("remotebitbang", default=True, description="build with remote bitbang support")
    variant("ftdi", default=True, description="build with ftdi support")
    variant("linuxgpiod", default=True, description="build with linux gpio support")
    variant("bcm2835gpio", default=True, description="build with bcm2835gpio support")

    depends_on("automake", type="build")
    depends_on("autoconf", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("libtool", type="build")
    depends_on("libusb", type="build", when="+ftdi")
    depends_on("libftdi", type="build", when="+ftdi")
    depends_on("libgpiod@:1.6", type="build", when="+linuxgpiod")
    depends_on("jimtcl@:0.79", type="build", when="@2025.03.31:")

    def autoreconf(self, spec, prefix):
        Executable("./bootstrap")()

    def configure_args(self):
        spec = self.spec
        args = []

        if spec.satisfies("+remotebitbang"):
            args.append("--enable-remote-bitbang")
        args.extend(self.enable_or_disable("ftdi"))
        args.extend(self.enable_or_disable("linuxgpiod"))
        args.extend(self.enable_or_disable("bcm2835gpio"))

        return args

    def setup_run_environment(self, env):
        env.prepend_path("OPENOCD_SCRIPTS", f"{self.prefix}/share/openocd/scripts")
