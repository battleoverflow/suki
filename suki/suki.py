"""
    Owner: azazelm3dj3d (https://github.com/azazelm3dj3d)
    Project: Suki
    License: BSD 2-Clause
"""

import site, os, argparse, shutil

# Check out Faye, it's also one of my libraries
# 👀 https://github.com/shinigamilib/faye
from faye.faye import Faye

parser = argparse.ArgumentParser()

parser.add_argument('-v', '--version', help="Version information", action='store_true', default=None, required=False)
parser.add_argument('-l', '--link', help="Link all of your Python site packages, allowing you to access them from your current working directory (requires sudo/root privileges)", action='store_true', default=None, required=False)
parser.add_argument('-f', '--file', help="Absolute path to your requirements.txt file. Defaults to the current working directory", default="requirements.txt", required=False)

args = parser.parse_args()

class Suki():

    # Suki version
    def version() -> str:
        return "0.0.6"

    def banner():
        """
        🌸 Banner 🌸
        """
        
        print("-" * 26)
        print(f"🌸 (¬_¬) Suki | v{Suki.version()} 🌸")
        print("-" * 26)
        print("Owner: azazelm3dj3d (https://github.com/azazelm3dj3d)")
        print("Source: https://github.com/azazelm3dj3d/suki")
        print("\n")

    def link():
        """
        The most powerful method powering Suki.
        This allows the user to create a local directory of a set of packages.
        """

        # Have to delete the directory every run to refresh the symbolic links
        if os.path.isdir("suki_pkgs"):
            shutil.rmtree("suki_pkgs")
        
        packages = os.listdir(site.getsitepackages()[1])
        site_packages = site.getsitepackages()[1]

        # Irrelevant files/extensions in the site packages directory
        py_check = [
            "dist-info",
            "egg-info",
            "__pycache__",
            ".pyd"
        ]

        # Makes sure the requirements.txt file exists
        if os.path.exists(str(args.file)):
            with open(str(args.file), "r") as f:
                # Parses the requirements.txt file to locate required packages
                for fi in f:
                    # Parses the site packages directory for required packages
                    for p in packages:
                        # Removes irrelevant files/extensions from the result
                        for rm in py_check:
                            if rm not in p and p in fi:
                                # Checks if the packages directory already exists
                                if os.path.isdir("suki_pkgs"):
                                    try:
                                        # Symbolically links the site packages
                                        os.symlink(f"{site_packages}/{p}", f"suki_pkgs/{p}")
                                        Faye().progress(os.path.getsize(f"suki_pkgs/{p}"), f"{p}")
                                    except OSError as err:
                                        print(err)
                                else:
                                    # Creates the packages directory if it doesn't exist
                                    os.mkdir("suki_pkgs")

                                    try:
                                        # Symbolically links the site packages
                                        os.symlink(f"{site_packages}/{p}", f"suki_pkgs/{p}")
                                        Faye().progress(os.path.getsize(f"suki_pkgs/{p}"), f"{p}")
                                    except OSError as err:
                                        print(err)
                                
                                break
        else:
            print(f"Unable to locate requirements.txt at {str(args.file)}")
            exit(0)

    def main():
        """
        The main function for Suki
        """

        if args.version:
            print(f"v{Suki.version()}")

        if args.link:
            Suki.banner()
            Suki.link()

if __name__ == '__main__':
    Suki.main()