# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack.package import *


class ArmGnuToolchain(Package):
    """Arm GNU Toolchain is a community supported pre-built GNU compiler
    toolchain for Arm based CPUs.

    Provides the AArch32 bare-metal (arm-none-eabi) cross toolchain for Linux
    hosts. Binary releases are selected for the current host architecture
    (x86_64 or aarch64).

    Downloads come from the Arm GitLab package registry
    (tooling/gnu-toolchains-for-arm).
    """

    homepage = "https://gitlab.arm.com/tooling/gnu-toolchains-for-arm"
    # Placeholder; real URL comes from url_for_version based on host arch.
    url = (
        "https://gitlab.arm.com/api/v4/projects/tooling%2Fgnu-toolchains-for-arm/"
        "packages/generic/gnu-toolchain/15.3.rel1/"
        "arm-gnu-toolchain-15.3.rel1-aarch64-arm-none-eabi.tar.xz"
    )

    maintainers("davekeeshan")

    # Host arch -> sha256 for arm-none-eabi binary releases (from Arm .sha256asc).
    toolchain_releases = {
        "15.3.rel1": {
            "aarch64": "06979e0c8171de58e5dc2a2b2019330a290f30930f27728af98a83e1a7369b3a",
            "x86_64": "563bebb2b97d53382b956d6ee1fe61e2cae26699901417234a37df505ef9b5fa",
        },
        "15.2.rel1": {
            "aarch64": "d061559d814b205ed30c5b7c577c03317ec447ca51cd5a159d26b12a5bbeb20c",
            "x86_64": "597893282ac8c6ab1a4073977f2362990184599643b4c5ee34870a8215783a16",
        },
        "14.3.rel1": {
            "aarch64": "2d465847eb1d05f876270494f51034de9ace9abe87a4222d079f3360240184d3",
            "x86_64": "8f6903f8ceb084d9227b9ef991490413014d991874a1e34074443c2a72b14dbd",
        },
        "14.2.rel1": {
            "aarch64": "87330bab085dd8749d4ed0ad633674b9dc48b237b61069e3b481abd364d0a684",
            "x86_64": "62a63b981fe391a9cbad7ef51b17e49aeaa3e7b0d029b36ca1e9c3b2a9b78823",
        },
        "13.3.rel1": {
            "aarch64": "c8824bffd057afce2259f7618254e840715f33523a3d4e4294f471208f976764",
            "x86_64": "95c011cee430e64dd6087c75c800f04b9c49832cc1000127a92a97f9c8d83af4",
        },
        "13.2.rel1": {
            "aarch64": "8fd8b4a0a8d44ab2e195ccfbeef42223dfb3ede29d80f14dcf2183c34b8d199a",
            "x86_64": "6cd1bbc1d9ae57312bcd169ae283153a9572bd6a8e4eeae2fedfbc33b115fdbb",
        },
    }

    # GitLab package versions that differ from the spack version string.
    gitlab_version_names = {
        "13.2.rel1": "13.2.Rel1",
    }

    host_targets = {
        "aarch64": "aarch64",
        "arm64": "aarch64",
        "x86_64": "x86_64",
        "amd64": "x86_64",
    }

    _target = host_targets.get(platform.machine().lower(), platform.machine().lower())

    for release, arches in toolchain_releases.items():
        if _target in arches:
            version(release, sha256=arches[_target])

    def url_for_version(self, version):
        vstr = str(version)
        gver = self.gitlab_version_names.get(vstr, vstr)
        return (
            "https://gitlab.arm.com/api/v4/projects/tooling%2Fgnu-toolchains-for-arm/"
            f"packages/generic/gnu-toolchain/{gver}/"
            f"arm-gnu-toolchain-{gver}-{self._target}-arm-none-eabi.tar.xz"
        )

    def install(self, spec, prefix):
        install_tree(".", prefix)
