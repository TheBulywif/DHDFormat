from fmtInit import find_exempt
from format import format
from scanner import scan_new_drives, wait_new_conn



if __name__ == '__main__':
    while True:
        print(f"Building EXEMPT drive list...")
        EXEMPT = find_exempt.find_drives()
        print(f"Searching for new Storage Device...")
        wait_new_conn.scan(EXEMPT)
        archive, flash = scan_new_drives.find_drives(EXEMPT)
        EXEMPT = find_exempt.find_drives()

