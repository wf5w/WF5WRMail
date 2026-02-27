#!/usr/bin/env python

import subprocess
import sys
import os 

if len(sys.argv) == 1:
    print("usage: transferOutbox.py [ -d | remote-ip-address remote-user remote-callsign local-callsign ]")
    sys.exit()
elif len(sys.argv) == 2 and sys.argv[1] == '-d':
    remoteip = '10.42.0.1'
    remoteuser = 'pi'
    remotecallsign = 'NOCALL'
    localcallsign = 'NOCALL'
else:
    remoteip = sys.argv[1]
    remoteuser = sys.argv[2]
    remotecallsign = sys.argv[3]
    localcallsign = sys.argv[4]

remotecallsign = remotecallsign.upper()
localcallsign  = localcallsign.upper()

print(
    f"""parameters:  
      remote ip address: {remoteip}
      remote user:       {remoteuser}
      remote callsign:   {remotecallsign}
      local callsign:    {localcallsign}
      """)

home = os.environ['HOME']

localdir = f"{home}/.local/share/pat/mailbox/{localcallsign}/out"
os.chdir(localdir)

remotecmd = f"/usr/bin/ls -1 ~/.local/share/pat/mailbox/{remotecallsign}/out/* | wc -l"
cmd = ["ssh", f"{remoteuser}@{remoteip}", remotecmd ]

try:
    # Set capture_output=True to capture stdout and stderr
    # Set text=True to receive output as a string (instead of bytes)
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    nfiles = result.stdout
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
    print("Error output:", e.stderr)

print(f"number of files found: {nfiles}")

if nfiles:
    remotepath = f".local/share/pat/mailbox/{remotecallsign}/out/*"
    cmd = ["scp", f"{remoteuser}@{remoteip}:{remotepath}", "."]

    try:
        # Set capture_output=True to capture stdout and stderr
        # Set text=True to receive output as a string (instead of bytes)
        result = subprocess.run(cmd, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print("Error output:", e.stderr)

