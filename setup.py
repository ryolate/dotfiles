#!/usr/bin/env python3

import os
import sys
import argparse
import pathlib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", action='store_true',
                        help='overwrite existing files')
    args = parser.parse_args()

    cur = os.path.dirname(sys.argv[0])
    home = pathlib.Path.home()

    dotfiles(cur, home, args.force)


def dotfiles(cur: str, home: pathlib.Path, force: bool):
    for d in os.scandir(cur):
        if d.name[0] == "." or d.is_file():
            continue
        for f in os.listdir(d):
            src = os.path.abspath(os.path.join(cur, d.name, f))
            dst = os.path.join(home, f.replace('dot.', '.'))

            if os.path.exists(dst):
                if not force:
                    print(f"Skip {dst}; already exists")
                    continue

                backup = dst + ".old"
                print(f"Updating {dst}; backup {backup}")
                os.rename(dst, backup)

            print(f"{src} -> {dst}")
            os.symlink(src, dst)


if __name__ == "__main__":
    main()
