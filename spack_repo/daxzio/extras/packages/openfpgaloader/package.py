from spack.package import *
from spack_repo.builtin.packages.openfpgaloader.package import (
    Openfpgaloader as BuiltinOpenfpgaloader,
)


class Openfpgaloader(BuiltinOpenfpgaloader):
    """openFPGALoader - extended with additional versions."""

    # Custom version releases (add your own here)
    version("2026.02.26", commit="3ae5e5e4a5f055d12f6079616cb1ec1d67bf30f1")
    version("2026.09.09", commit="f6a678b4bba17ffa93b67a4eb95bc9afa1ac1a36")
