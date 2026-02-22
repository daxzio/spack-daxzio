
from spack.package import *
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

class Nvc(AutotoolsPackage):
    """NVC is a VHDL compiler and simulator."""

    homepage = "https://www.nickg.me.uk/nvc/"
    git = "https://github.com/nickg/nvc.git"
    url = "https://github.com/nickg/nvc/archive/refs/tags/r1.18.1.tar.gz"
    license("GPL-3.0-or-later")

    maintainers("davekeeshan")
    
    version("master", branch="master")
    
    version(
        "1.18.1", 
        sha256="9bf856b2fb8916bea0082762a642bf259b87fcff1eeda1aa3382451c38a8e2f9", 
    )

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool",  type="build")
    depends_on("llvm@19", type=("build", "link"))
    
    build_directory = "build"
 
    def autoreconf(self, spec, prefix):
        autoreconf = which("autoreconf")
        autoreconf("-fiv")
    
    def setup_build_environment(self, env):
        """Set up build environment to find LLVM."""
        # Add LLVM bin directory to PATH so llvm-config can be found
        env.prepend_path("PATH", self.spec["llvm"].prefix.bin)
        # Add LLVM lib directory to library paths
        env.prepend_path("LD_LIBRARY_PATH", self.spec["llvm"].prefix.lib)
    
    def configure_args(self):
        """Arguments to pass to configure."""
        args = []
        
        # Pass the full path to llvm-config (following proj/tcl_tclxml pattern)
        # This ensures we use the Spack-installed LLVM's llvm-config
        llvm_config_path = self.spec["llvm"].prefix.bin.join("llvm-config")
        args.append(f"--with-llvm={llvm_config_path}")
        args.append("--enable-llvm")
        
        # Use static LLVM libraries since LLVM was built with dylib
        # which provides monolithic libLLVM.so instead of separate .so files
        args.append("--enable-static-llvm")
        
        return args
