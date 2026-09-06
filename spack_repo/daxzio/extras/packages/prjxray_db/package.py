# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class PrjxrayDb(Package):
    """Prebuilt Project X-Ray device databases for Xilinx 7-series FPGAs.

    Device pin maps, segbits, and part metadata used by nextpnr-xilinx
    (chipdb generation) and prjxray (FASM to bitstream conversion).
    """

    homepage = "https://github.com/openXC7/prjxray-db"
    git = "https://github.com/openXC7/prjxray-db.git"

    maintainers("davekeeshan")

    license("CC0-1.0")

    version("master", branch="master")
    version("0.9.1", tag="0.9.1")

    def install(self, spec, prefix):
        db_root = join_path(prefix, "share", "prjxray-db")
        mkdirp(db_root)
        for entry in os.listdir("."):
            if entry.startswith("."):
                continue
            src = join_path(".", entry)
            if os.path.isdir(src):
                install_tree(src, join_path(db_root, entry))

    def setup_run_environment(self, env):
        env.set("PRJXRAY_DB_DIR", join_path(self.prefix, "share", "prjxray-db"))
