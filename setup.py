import subprocess
import sys
def install_modules(modules):
    for module in modules:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
modules_to_install = ["sc-compression"]
install_modules(modules_to_install)