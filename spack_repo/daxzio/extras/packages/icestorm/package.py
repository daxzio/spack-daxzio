# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.build_systems.makefile import MakefilePackage

class Icestorm(MakefilePackage):
    """Project IceStorm aims at documenting the bitstream format of Lattice iCE40
    
    FPGAs and providing simple tools for analyzing and creating bitstream files. 
    """

    homepage = "https://github.com/YosysHQ/icestorm"
    git = "https://github.com/YosysHQ/icestorm.git"

    maintainers("davekeeshan")

    license("ISC")

    version("master", branch="master")

    def install(self, spec, prefix):
        make("install", f"DESTDIR={prefix}", "PREFIX=/")
