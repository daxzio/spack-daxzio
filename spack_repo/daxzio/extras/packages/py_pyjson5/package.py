# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import shutil

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyjson5(PythonPackage):
    """Python implementation of the JSON5 data format (Kijewski fork).

    Required by Project X-Ray Python libraries. This is distinct from the
    unrelated py-json5 Spack package (dpranke/json5 on PyPI).
    """

    homepage = "https://github.com/Kijewski/pyjson5"
    git = "https://github.com/Kijewski/pyjson5.git"

    maintainers("davekeeshan")

    license("MPL-2.0")

    version("master", branch="master")
    version(
        "2024.08.19",
        commit="1f03f9ebb6632b700e94cd4ce9bb7e6efc5fb139",
    )

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("fast-double-parser", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")

    def _fast_double_parser_header(self):
        return join_path(
            self.stage.source_path,
            "third-party",
            "fast_double_parser",
            "include",
            "fast_double_parser.h",
        )

    @run_before("install")
    def prepare_fast_double_parser(self):
        """Populate pyjson5's vendored header path before pip builds the extension."""
        header = self._fast_double_parser_header()
        if os.path.isfile(header):
            return

        third_party = join_path(self.stage.source_path, "third-party")
        mkdirp(third_party)
        dest = join_path(third_party, "fast_double_parser")
        if os.path.lexists(dest):
            if os.path.islink(dest):
                os.remove(dest)
            elif os.path.isdir(dest):
                shutil.rmtree(dest)

        src = join_path(
            self.spec["fast-double-parser"].prefix, "share", "fast-double-parser"
        )
        install_tree(src, dest)

        if not os.path.isfile(header):
            raise InstallError(
                "failed to install fast-double-parser headers into py-pyjson5 source tree"
            )
