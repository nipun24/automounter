# Automounter

Keeps network shares mounted and remounts them if disconnected

Add this to crontab to check if network share is mounted or not every 2 minutes

```bash
# edit the path of executables accordingly
# use flock to avoid duplicate crobjobs
*/2 * * * * /bin/flock /Users/web/automounter.lock -c '/bin/python3 /Users/web/main.py &> /Users/web/cron.log'
```