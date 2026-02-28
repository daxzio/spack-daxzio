# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack.package import *


class GnatFsf(Package):
    """The GNAT Ada compiler (FSF/GNU variant). Ada is a modern programming language
    designed for large, long-lived applications - and embedded systems in particular
    - where reliability and efficiency are essential.

    This package provides pre-built GNAT binaries from the Alire GNAT-FSF-builds
    project. Binary-only; supports Linux x86_64 and aarch64, and Darwin x86_64/aarch64.
    """

    homepage = "https://github.com/alire-project/GNAT-FSF-builds"

    # Binary releases from GNAT-FSF-builds (Alire project).
    # Native compilers: gnat-{arch}-{os}-{version}.tar.gz
    gnat_releases = {
        "15.2.0.1": {
            "linux": {
                "x86_64": "4640d4b369833947ab1a156753f4db0ecd44b0f14410b5b2bc2a14df496604bb",
                "aarch64": "54b1000a1b85f0ec241c71d375bae7602239875a01132f5dc5789a632870a1c7",
            },
            "darwin": {
                "x86_64": "fffe07e8732738a33e6ddc209debc23640e9e629584d30ad8ebee278999c7a0f",
                "aarch64": None,
            },
        },
        "14.2.0.1": {
            "linux": {
                "x86_64": "06bb3def7f70371d601a5c8b93bc4933c50873a5e5ba26aa7ee3447dda687722",
                "aarch64": "a28acec19866f46135594d7a1c6cca6085396598a256d03a4d01d8cb83f517dd",
            },
            "darwin": {
                "x86_64": None,
                "aarch64": None,
            },
        },
        "12.2.0.1": {
            "linux": {
                "x86_64": "11f3b811e4967bd4924a8236e9e68e0b9464fee016cd9d00c077faec0c27fe99",
                "aarch64": None,  # 12.2 may not have aarch64
            },
            "darwin": {
                "x86_64": None,
                "aarch64": None,
            },
        },
    }

    gnat_targets = {
        "aarch64": "aarch64",
        "arm64": "aarch64",
        "amd64": "x86_64",
        "x86_64": "x86_64",
    }

    # Filename patterns: gnat-{arch}-{os}-{version_suffix}.tar.gz
    gnat_filenames = {
        "linux": {
            "x86_64": "x86_64-linux",
            "aarch64": "aarch64-linux",
        },
        "darwin": {
            "x86_64": "x86_64-darwin",
            "aarch64": "aarch64-darwin",
        },
    }

    os_name = platform.system().lower()
    target = gnat_targets.get(platform.machine().lower(), platform.machine().lower())

    for ver, platforms in gnat_releases.items():
        for os_key, archs in platforms.items():
            if os_key == os_name and archs.get(target):
                version(ver, sha256=archs[target])
                break

    def url_for_version(self, version):
        if self.os_name not in ("linux", "darwin"):
            return None
        if self.os_name not in self.gnat_filenames or self.target not in self.gnat_filenames[self.os_name]:
            return None
        releases = getattr(self, "gnat_releases", {})
        if str(version) not in releases:
            return None
        platforms = releases[str(version)]
        if self.os_name not in platforms or self.target not in platforms[self.os_name] or not platforms[self.os_name][self.target]:
            return None
        suffix = self.gnat_filenames[self.os_name][self.target]
        ver_str = str(version)
        if "12.2" in ver_str:
            tag, ver_suffix = "gnat-12.2.0-1", "12.2.0-1"
        elif "14.2" in ver_str:
            tag, ver_suffix = "gnat-14.2.0-1", "14.2.0-1"
        elif "15.2" in ver_str:
            tag, ver_suffix = "gnat-15.2.0-1", "15.2.0-1"
        else:
            return None
        return f"https://github.com/alire-project/GNAT-FSF-builds/releases/download/{tag}/gnat-{suffix}-{ver_suffix}.tar.gz"

    def install(self, spec, prefix):
        install_tree(".", prefix)
