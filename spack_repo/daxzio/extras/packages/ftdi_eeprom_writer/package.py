# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.build_systems.makefile import MakefilePackage


class FtdiEepromWriter(MakefilePackage):
    """Small utility to read and write the EEPROM of FTDI FT2232H devices,
    setting the serial number, PID/VID, manufacturer and device description
    fields."""

    homepage = "https://github.com/yogggoy/ftdi_eeprom_writer"
    git = "https://github.com/yogggoy/ftdi_eeprom_writer.git"

    maintainers("davekeeshan")

    license("GPL-2.0-only")

    version("master", branch="master")
    version("2026.02.06", commit="c5d54de2dc8bcfee02194ef3b59db530bc28eb5e")

    depends_on("c", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("libftdi")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("ftdi-eeprom-config", prefix.bin)
