# rename to env.py

# add more to the array if necessary
SHARES = ['smb://<username>:<password>@<host>/<path>', 'smb://<username>:<password>@<host>/<path>']

BASE_PATH = '/Volumes' # this is /Volumes for MACOS
ENABLE_HEALTHCHECK = True # false if you do not have healcheck endpoint configured
HEALTHCHECK_URL = '' # your healthcheck endpoint; leave blank if ENABLE_HEALTHCHECK = False