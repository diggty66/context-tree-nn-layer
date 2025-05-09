
"""
verify_env.py

This script checks for:
- Python version compatibility (3.9.x)
- pip/setuptools/wheel version status
- Project installability with editable mode
"""

import sys
import subprocess
import pkg_resources
import shutil

def check_python_version():
    major, minor = sys.version_info[:2]
    if major != 3 or minor != 9:
        print(f"❌ Python 3.9.x is required, found {sys.version}")
        return False
    print(f"✅ Python version OK: {sys.version}")
    return True

def check_package_versions():
    success = True
    expected = {
        'pip': '23.0.0',
        'setuptools': '67.0.0',
        'wheel': '0.40.0'
    }
    for pkg, min_ver in expected.items():
        try:
            version = pkg_resources.get_distribution(pkg).version
            if pkg_resources.parse_version(version) < pkg_resources.parse_version(min_ver):
                print(f"❌ {pkg} is too old ({version} < {min_ver})")
                success = False
            else:
                print(f"✅ {pkg} version OK: {version}")
        except pkg_resources.DistributionNotFound:
            print(f"❌ {pkg} is not installed")
            success = False
    return success

def check_gitbash_admin():
    try:
        import ctypes
        if ctypes.windll.shell32.IsUserAnAdmin():
            print("✅ Git Bash is running as Administrator")
            return True
        else:
            print("⚠️  Not running as Administrator — may cause install errors")
            return False
    except Exception:
        print("ℹ️  Admin check not available")
        return True

def check_editable_install():
    if not shutil.which("python"):
        print("❌ Python not found in PATH")
        return False
    result = subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."],
                            capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Editable install worked")
        return True
    else:
        print("❌ Editable install failed:\n", result.stderr.splitlines()[-10:])
        return False

if __name__ == "__main__":
    print("🔍 Verifying environment...")
    all_ok = all([
        check_python_version(),
        check_package_versions(),
        check_gitbash_admin(),
        check_editable_install()
    ])
    print("✅ Environment verified!" if all_ok else "❌ Issues found. See above.")
