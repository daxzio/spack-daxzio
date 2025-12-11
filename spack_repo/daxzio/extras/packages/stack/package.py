# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Stack(Package):
    homepage = "https://docs.haskellstack.org/"
    url = "https://github.com/commercialhaskell/stack/releases/download/v3.7.1/stack-3.7.1-linux-x86_64.tar.gz"

    version(
        "3.7.1",
        sha256="b6df9168d471d917d955ee80553562ca2b0b3b1aa61cd1256199406c2d8c4eb4",
    )

    def install(self, spec, prefix):
        install_tree(".", prefix)
