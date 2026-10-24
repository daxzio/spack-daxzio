# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.build_systems.cargo import CargoPackage


class Xezim(CargoPackage):
    """Open-source SystemVerilog simulator written in Rust.

    Event-driven, 4-state, IEEE 1800-2023, with UVM, DPI, and VPI.
    """

    homepage = "https://github.com/aionhw/xezim"
    git = "https://github.com/aionhw/xezim.git"

    maintainers("davekeeshan")

    license("Apache-2.0 OR MIT")

    version("main", branch="main")
    version(
        "0.11.3",
        tag="0.11.3",
        commit="058f2bba58648452e5799d17572356ebcae7d163",
    )
    version(
        "0.11.2",
        tag="0.11.2",
        commit="6fe99100cf4cb027216561a0fa48c038d1ecd3a0",
    )
    version(
        "0.11.1",
        tag="0.11.1",
        commit="b3994794dbf7560be7c73ab37bcaf6269f696320",
    )
    version(
        "0.11.0",
        tag="0.11.0",
        commit="6558a1e64e251cbd8d0c4e936860af268cf7e04f",
    )

    depends_on("rust@1.92:", type="build")
    depends_on("c", type="build")
    depends_on("git", type="build")
    depends_on("gmake", type="build")

    def setup_build_environment(self, env):
        # xezim-core is a pinned git dependency; libgit2 often fails on GitHub.
        env.set("CARGO_NET_GIT_FETCH_WITH_CLI", "true")
        # build.rs clones a UVM tree used only by integration tests.
        env.set("XEZIM_UVM_DIR", "skip")
