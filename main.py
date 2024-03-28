from urllib.parse import urlparse
import urllib.request
import os
from datetime import datetime
from env import *
from time import sleep

if __name__ == "__main__":
    print(datetime.now())

    flag = True
    for i in SHARES:
        res = urlparse(i)
        exit_code = os.system(f'/sbin/ping -c 1 {res.hostname}')
        if exit_code == 0:
            mount_path = BASE_PATH + res.path
            # check if path exists
            if os.path.exists(mount_path):
                # check if path is writable
                if os.access(mount_path, os.W_OK):
                    print(f'{mount_path} already mounted')
                else:
                    print("NOT WRITABLE!!!")
                    urllib.request.urlopen(HEALTHCHECK_URL + 'fail',
                                timeout=10)
            else:
                os.system(f'open {i}')
                sleep(10)
                print(f'mounted {mount_path}')
        else:
            print(exit_code)
            flag = False

    if ENABLE_HEALTHCHECK:
        if flag:
            urllib.request.urlopen(HEALTHCHECK_URL,
                                timeout=10)
        else:
            urllib.request.urlopen(HEALTHCHECK_URL + 'fail',
                                timeout=10)
