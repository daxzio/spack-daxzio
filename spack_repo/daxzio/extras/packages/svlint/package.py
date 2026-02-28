# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.build_systems.cargo import CargoPackage


class Svlint(CargoPackage):
    """SystemVerilog linter compliant with IEEE1800-2017.

    Written in Rust, based on sv-parser.
    """

    homepage = "https://github.com/dalance/svlint"
    url = "https://github.com/dalance/svlint/archive/refs/tags/v0.9.3.tar.gz"
    git = "https://github.com/dalance/svlint.git"

    maintainers("davekeeshan")

    license("MIT")

    version("master", branch="master")
    version(
        "0.9.5",
        sha256="1ffa212d571eabf57fb2b32c648760a0aff301dff8282a5a2b8e653d4657d3fe",
    )
    version(
        "0.9.4",
        sha256="989555c119fb24b93aaec3ebf4dc8a4469f8a61880f7482683316180a2062a54",
    )
    version(
        "0.9.3",
        sha256="ed07d77dd72fe49c086df407ed74e321d210eb19dc0dc353ebcf23414116ccfd",
    )
