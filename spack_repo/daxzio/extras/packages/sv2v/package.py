# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.makefile import MakefilePackage


class Sv2v(MakefilePackage):
    """sv2v converts SystemVerilog (IEEE 1800-2017) to Verilog (IEEE 1364-2005),
    with an emphasis on supporting synthesizable language constructs."""

    homepage = "https://ghdl.github.io/ghdl"
    git = "https://github.com/zachjs/sv2v.git"
    url = "https://github.com/zachjs/sv2v/archive/refs/tags/v0.0.13.tar.gz"

    license("GPL-2.0-or-later")

    maintainers("davekeeshan")

    version("master", branch="master")
    version(
        "0.0.13",
        sha256="4ce7df8c6fa3857da6a2b69343c29e7c627a4283090f2b07221aa9ef956a88c8",
    )

    depends_on("stack")

    def build(self, spec, prefix):
        # This will call 'make' by default
        make()

    def install(self, spec, prefix):
        # Custom installation if 'make install' isn't supported
        mkdirp(prefix.bin)
        install("bin/sv2v", prefix.bin)
