from spack.package import *
from spack_repo.builtin.packages.icarus.package import Icarus as BuiltinIcarus


class Icarus(BuiltinIcarus):
    """Icarus Verilog - extended with additional versions."""

    version("2026.02.20", commit="9b44d55e9a568173e8264f882280775346fdff81")
