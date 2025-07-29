# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *

class Openocd(AutotoolsPackage):
    """The Open On-Chip Debugger (OpenOCD) aims to provide debugging, in-system
    programming and boundary-scan testing for embedded target devices.
    """

    homepage = "https://openocd.org/"
    url = "https://github.com/openocd-org/openocd/archive/refs/tags/v0.12.0.tar.gz"
    git = "https://github.com/openocd-org/openocd.git"

    maintainers("davekeeshan")

    license("GPL-2.0-or-later")

    version("master", branch="master")

    version("2025.07.29", commit="6872f7e406ad74f366f55947d23becd5a5faca15")
    version("2025.05.09", commit="744955e5b4f4f943c187622f4ae977bc4cd6fdb7")
    version("2025.03.01", commit="a168c634126e9e6bb95c6e68b2db5afbb099abf7")
    version("2025.01.09", commit="d4b3b4ea82ba6d34b050a1cc068e0b105533e2f2", submodules=True)
    version("0.12.0", commit="9ea7f3d647c8ecf6b0f1424002dfc3f4504a162c", submodules=True)

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
    depends_on("jimtcl@:0.79", type="build", when="@2025.03.01:")
    depends_on("libusb", type="build", when="+ftdi")
    depends_on("libftdi", type="build", when="+ftdi")
    depends_on("libgpiod@:1.6", type="build", when="+linuxgpiod")

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
