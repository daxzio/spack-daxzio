# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.build_systems.cmake import CMakePackage


class Prjtrellis(CMakePackage):
    """Project Trellis enables a fully open-source flow for ECP5 FPGAs using
    Yosys for Verilog synthesis and nextpnr for place and route. Project
    Trellis itself provides the device database and tools for bitstream
    creation.
    """

    homepage = "https://github.com/YosysHQ/prjtrellis"
    git = "https://github.com/YosysHQ/prjtrellis.git"

    maintainers("davekeeshan")

    license("ISC")

    version("master", branch="master", submodules=True)


#     def build(self, pkg, spec, prefix):
