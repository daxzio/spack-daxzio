# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage


class PyApicula(PythonPackage):
    """Project Apicula uses a combination of fuzzing and parsing of the vendor
    data files to provide Python tools for generating bitstreams.
    """

    homepage = "https://github.com/YosysHQ/apicula"
    url = "https://github.com/YosysHQ/apicula/archive/refs/tags/0.21.tar.gz"
    git = "https://github.com/daxzio/apicula.git"

    maintainers("davekeeshan")

    license("MIT")

    #     version("master", branch="master", submodules=True)
    #     version("0.21", sha256="f6b5341a56898f3584afd98aaa44162db9b9ee2b23fd6a7ef702dd5c7da8431c")
    version("0.20", commit="47b5d441af28f67333e19cd0d5c7038b5b239e4e")

    #     def build(self, pkg, spec, prefix):
    depends_on("python@3.8:3.10", type=("build", "run"))
    depends_on("py-setuptools", type="build")
