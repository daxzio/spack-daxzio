# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.build_systems.cargo import CargoPackage


class Radicle(CargoPackage):
    """Radicle Heartwood Protocol & Stack

    Heartwood is the third iteration of the Radicle Protocol, a powerful 
    peer-to-peer code collaboration and publishing stack. The repository contains 
    a full implemention of Heartwood, complete with a user-friendly command-line 
    interface (rad) and network daemon (radicle-node).

    Radicle was designed to be a secure, decentralized and powerful alternative 
    to code forges such as GitHub and GitLab that preserves user sovereignty 
    and freedom.
    """

    homepage = "https://radicle.xyz/"
    git = "https://seed.radicle.xyz/z3gqcJUoA1n9HaHKufZs5FCSGazv5.git"

    maintainers("davekeeshan")

    license("MIT")

    version("master", branch="master")
    version("1.2.1", commit="29043134a361aa8931cd069a1c72e3d2e8deae97")


    def build(self, spec, prefix):
        cargo("install", "--root", "out", "--path", "crates/radicle-cli")
        cargo("install", "--root", "out", "--path", "crates/radicle-node")
        cargo("install", "--root", "out", "--path", "crates/radicle-remote-helper")
#         cargo("install", "--path", "crates/radicle-node",  "--force", "--locked")
#         cargo("install", "--root", prefix, "--path", "crates/radicle-remote-helper",  "--force", "--locked")

#     def build(self, spec, prefix):
#         # The carogopackage installer doesn't allow for an option to install from a subdir
#         # see: https://github.com/rust-lang/cargo/issues/7599
#         cargo("install", "--root", prefix, "--path", "crates/radicle-cli",  "--force", "--locked")
#         cargo("install", "--root", prefix, "--path", "crates/radicle-node",  "--force", "--locked")
#         cargo("install", "--root", prefix, "--path", "crates/radicle-remote-helper",  "--force", "--locked")
#         cargo("install", "--root", "out", "bindgen-cli")
