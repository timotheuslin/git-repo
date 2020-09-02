import os
import sys
import subprocess
import win32elevate

if __name__ == '__main__':
    win32elevate.elevateAdminRights(reattachConsole=True)
    new_argv = subprocess.list2cmdline([sys.executable] + sys.argv[1:])
    rc = os.system(new_argv)
    print("rc:%d" % rc)
    sys.exit(rc)
