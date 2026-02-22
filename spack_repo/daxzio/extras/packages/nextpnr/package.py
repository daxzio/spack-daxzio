# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.build_systems.cmake import CMakePackage

class Nextpnr(CMakePackage):
    """SystemVerilog linter compliant with IEEE1800-2017. 
    
    Written in Rust, based on sv-parser. 
    """

    homepage = "https://github.com/YosysHQ/nextpnr"
#     url = "https://github.com/YosysHQ/nextpnr/archive/refs/tags/nextpnr-0.8.tar.gz"
    git = "https://github.com/YosysHQ/nextpnr.git"

    maintainers("davekeeshan")

    license("MIT")

    version("master", branch="master", submodules=True)
    version("0.8.1", commit="b0626280e99d43edf1d2e086bb1459751e81519e", submodules=True)
    version("0.8", commit="0c01cb9e4182506df6cada050afca09f0d7a001f", submodules=True)
#     version("0.8", sha256="968ce3f39973e1d855c6bf1606a334d9f9650cff978554b822de0a6c088947bd")
    
    depends_on("boost+filesystem+thread+program_options+iostreams", type=("build", "link"))
    depends_on("eigen")
    depends_on("python@3.9:", type=("build", "run"))

    depends_on("icestorm")
#     depends_on("py-apicula")

    # CMake options
    def cmake_args(self):
        spec = self.spec

        args = []
        args.append("-DARCH=generic;ice40;himbaechel")
        args.append('-DHIMBAECHEL_UARCH=gowin')
        args.append(f"-DICESTORM_INSTALL_PREFIX={spec['icestorm'].prefix}")
        args.append(f"-DAPYCULA_INSTALL_PREFIX=/home/gomez/temp/apicula/apycula")
        
        return args
