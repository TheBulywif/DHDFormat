# FIND DRIVES ON COMPUTER THAT ARE TO BE EXEMPT FROM FORMATTING
import os
import psutil

EXEMPT = []


def find_drives():
    templ = "%-17s"
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        EXEMPT.append(part.device)
    return EXEMPT


if __name__ == '__main__':
    find_drives()
