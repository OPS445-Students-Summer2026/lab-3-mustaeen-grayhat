#!/usr/bin/env python3

# Author ID: mmasad

import subprocess


def free_space():
    process = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        shell=True,
        stdout=subprocess.PIPE
    )

    output = process.communicate()

    stdout = output[0].decode('utf-8').strip()

    return stdout


if __name__ == '__main__':
    print(free_space())
