from urllib.parse import urlparse
import urllib.request
import os
from datetime import datetime
from env import *

if __name__ == "__main__":
    print(datetime.now())

    flag = True
    for i in SHARES:
        res = urlparse(i)
        exit_code = os.system(f'/sbin/ping -c 1 {res.hostname}')
        if exit_code == 0:
            mount_path = BASE_PATH + res.path
            if os.path.exists(mount_path):
                print(f'{mount_path} already mounted')
            else:
                os.system(f'open {i}')
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
