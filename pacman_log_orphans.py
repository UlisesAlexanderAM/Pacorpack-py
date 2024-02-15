#!/usr/bin/env python

import subprocess


def main():
    try:
        orphan_packages_command = subprocess.run(
            args=["pacman", "-Qdtq"], capture_output=True, check=True, encoding="utf-8"
        )
        orphan_packages = orphan_packages_command.stdout
        msg = f"""
        The following packages are installed but not required (anymore):
        {orphan_packages}
        You can mark them as explicitly installed with \'pacman  -D --asexplicit <pkg>\'
        or remove them all using \'pacman -Qdtq | pacman -Rns\'"""
        print(msg)
    except subprocess.CalledProcessError as exc:
        if exc.returncode == 1:
            print("No orphan packages found")
        else:
            print(
                "Procces failed because did not return a succesful return code."
                f"Returned {exc.returncode}"
                f"{exc}"
            )


if __name__ == "__main__":
    main()
