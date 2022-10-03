import os
import psutil
from psutil._common import bytes2human


def find_drives(list):
    archive = []
    flash = []
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)
        total = bytes2human(usage.total)
        appTotal = total[:-1]
        if part.device not in list:
            if "T" in total:
                archive.append(part.device)
            elif "G" in total:
                if 300.0 > float(appTotal) > 28.0:
                    flash.append(part.device)
                elif float(appTotal) > 0 and float(appTotal) > 300:
                    archive.append(part.device)
            elif "M" in total:
                pass
    print(f"ARCHIVE: {archive}")
    print(f"FLASH: {flash}")
    return archive, flash


if __name__ == '__main__':
    archive, flash = find_drives(list)
