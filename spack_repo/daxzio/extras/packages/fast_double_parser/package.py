# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class FastDoubleParser(Package):
    """Fast C++ number parsing library (header-only).

    Vendored by pyjson5 for its Cython extension. Installed with the same
    include/ layout as upstream so dependents can symlink it into a source tree.
    """

    homepage = "https://github.com/lemire/fast_double_parser"
    git = "https://github.com/lemire/fast_double_parser.git"

    maintainers("davekeeshan")

    license("Apache-2.0", "BSL-1.0")

    version("master", branch="master")
    version(
        "2025.05.27",
        commit="0f1fe9902d25847c8348e2f93ddc9dbe5521eab6",
    )

    def install(self, spec, prefix):
        root = join_path(prefix, "share", "fast-double-parser")
        install_tree("include", join_path(root, "include"))

    def setup_run_environment(self, env):
        env.prepend_path(
            "CPATH", join_path(self.prefix, "share", "fast-double-parser", "include")
        )
