# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack.package import *


class Stack(Package):
    """Haskell Stack (binary package)."""

    homepage = "https://docs.haskellstack.org/"
    url = "https://github.com/commercialhaskell/stack/releases/download/v3.7.1/stack-3.7.1-linux-x86_64.tar.gz"

    maintainers("davekeeshan")

    # Binary releases per architecture (linux only).
    # Pattern follows rust_bootstrap: register version() only for current platform.
    stack_releases = {
        "3.7.1": {
            "aarch64": "752321c6af6bc88960a086ebd9ede72937a567f312842a29deb2ddc9ab316a20",
            "x86_64": "b6df9168d471d917d955ee80553562ca2b0b3b1aa61cd1256199406c2d8c4eb4",
        },
    }

    # Map platform.machine() to Stack's arch names
    stack_targets = {
        "aarch64": "aarch64",
        "arm64": "aarch64",
        "x86_64": "x86_64",
        "amd64": "x86_64",
    }

    # Current platform at package load (used for version registration and url_for_version)
    _os = platform.system().lower()
    _target = stack_targets.get(platform.machine().lower(), platform.machine().lower())

    for release, arches in stack_releases.items():
        if _target in arches:
            version(release, sha256=arches[_target])

    def url_for_version(self, version):
        # Support spack checksum stack@3.7.1-linux-aarch64 for other arches
        vstr = str(version)
        if "-linux-" in vstr:
            base, _, arch = vstr.partition("-linux-")
            target = arch or self._target
        else:
            base = vstr
            target = self._target
        return f"https://github.com/commercialhaskell/stack/releases/download/v{base}/stack-{base}-linux-{target}.tar.gz"

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("stack", prefix.bin)
