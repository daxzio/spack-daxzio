# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFasm(PythonPackage):
    """FPGA Assembly (FASM) parser and generation library.

    Provides the Python ``fasm`` module used by Project X-Ray's fasm2frames
    utility. The ANTLR C++ parser is optional; if the native extension fails
    to build, the pure-Python textx parser is used instead.
    """

    homepage = "https://github.com/openXC7/fasm"
    git = "https://github.com/openXC7/fasm.git"

    maintainers("davekeeshan")

    license("Apache-2.0")

    version("master", branch="master")
    version(
        "2026.03.01",
        commit="2f57ccb1727a120e8cacbb95c578f3c71bdcc95a",
    )

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-textx", type=("build", "run"))
