# SCAN FOR NEW DRIVES TO BE CONNECTED
import os
import time

import psutil


def scan(list):
    tempList = []
    loop = True
    while loop:
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            if part.device not in tempList:
                tempList.append(part.device)
                print(f"{part.device} added to tempList")
        if len(tempList) > len(list):
            print(f"New drive detected. Looking for secondary drive.")
            for i in range(15):
                time.sleep(1)
                for part in psutil.disk_partitions(all=False):
                    if os.name == 'nt':
                        if 'cdrom' in part.opts or part.fstype == '':
                            continue
                    if part.device not in tempList:
                        tempList.append(part.device)
                        print(f"{part.device} added to tempList")
            print(f"Breaking Loop")
            loop = False
