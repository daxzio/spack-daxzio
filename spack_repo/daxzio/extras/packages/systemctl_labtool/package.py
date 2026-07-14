# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class SystemctlLabtool(Package):
    """Xilinx System Controller labtool: prebuilt hw_server, cs_server and
    xvc_server binaries together with the XSDB TCL scripts used to drive JTAG
    over Xilinx Virtual Cable from a board's system controller.

    Note: the shipped binaries are aarch64 ELF executables intended to run on
    the ARM system controller of Xilinx evaluation boards."""

    homepage = "https://github.com/Xilinx/systemctl-labtool"
    git = "https://github.com/Xilinx/systemctl-labtool.git"

    maintainers("davekeeshan")

    license("MIT")

    # Ships prebuilt aarch64 ELF binaries; only usable on the ARM system
    # controller of Xilinx evaluation boards.
    requires(
        "target=aarch64:",
        msg="systemctl-labtool ships prebuilt aarch64 binaries; it can only "
        "be installed for an aarch64 target",
    )

    # Tagged release
    version("2026_SC_Q2", tag="2026_SC_Q2")

    # Release branches (versions track upstream xlnx_rel_v* branches)
    version("2026.1", branch="xlnx_rel_v2026.1")
    version("2025.2", branch="xlnx_rel_v2025.2")
    version("2025.1", branch="xlnx_rel_v2025.1")
    version("2024.2", branch="xlnx_rel_v2024.2")
    version("2024.1", branch="xlnx_rel_v2024.1")
    version("2023.2", branch="xlnx_rel_v2023.2")
    version("2023.1", branch="xlnx_rel_v2023.1")
    version("2022.2", branch="xlnx_rel_v2022.2")
    version("2022.1", branch="xlnx_rel_v2022.1")
    version("2021.2", branch="xlnx_rel_v2021.2")

    # Development branches
    version("2024.1dev", branch="2024.1dev")
    version("2023.2dev", branch="2023.2dev")

    version("master", branch="master")

    def install(self, spec, prefix):
        # Prebuilt distribution: install the file tree verbatim, preserving
        # the usr/, etc/, 3rd_party/ and license/ layout and file modes.
        install_tree(".", prefix)

    def setup_run_environment(self, env):
        vitis = self.prefix.usr.local.xilinx_vitis
        env.prepend_path("PATH", self.prefix.usr.local.bin)
        env.prepend_path("PATH", vitis)
        env.set("XILINX_VITIS", vitis)
        env.set("TCLLIBPATH", vitis)
        env.set("TCL_LIBRARY", self.prefix.usr.local.lib.join("tcl8.5"))
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.usr.lib)
