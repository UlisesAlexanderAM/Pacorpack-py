#!/usr/bin/env python

import subprocess

orphan_packages_command = subprocess.run(args=["pacman","-Qdtq"],capture_output=True,check=True)
orphan_packages = orphan_packages_command.stdout.decode("utf-8")
msg = f"""
The following packages are installed but not required (anymore):
{orphan_packages}
You can mark them as explicitly installed with \'pacman  -D --asexplicit <pkg>\'
or remove them all using \'pacman -Qdtq | pacman -Rns\'"""
no_pkgs_msg="No orphan packages found"

def main():
    if orphan_packages_command.returncode == 0:
        print(msg)
    else:
        print(no_pkgs_msg)

if __name__ == '__main__':
    main()
