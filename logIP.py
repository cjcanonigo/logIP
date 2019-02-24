#!/usr/local/bin/python3

import subprocess
import datetime as dt
from slackclient import SlackClient
import sys
import os


def touch(path):
    # Creates empty file
    with open(path, 'a'):
        os.utime(path, None)


# Log Vars
currIP = 'currIP.txt'
histIP = 'histIP.txt'

# Slack Vars
sameIP = False

# Set Credentials
if len(sys.argv) > 1:
    slackToken = sys.argv[1]
    slackChannel = sys.argv[2]


# Make sure these files exist
touch(currIP)
touch(histIP)

# Run IP Command
cmd = ['dig', '@resolver1.opendns.com', 'ANY', 'myip.opendns.com', '+short']
result = subprocess.run(cmd, stdout=subprocess.PIPE)
ip = result.stdout.decode('utf-8')

# Build Timestamp
now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S | ")

# Check if IP changed
with open(currIP, 'r+') as f:
    first_line = f.readline()
    if first_line == ip:
        sameIP = True
    else:
        print('ip has changed from {}'.format(first_line))
    # always overwrite currIP file
    f.seek(0)
    f.write(ip)
    f.truncate()

# Save the IP to a log
with open(histIP, "a") as log:
    line = now + ip
    log.write(line)
    print(line)

# Slack Vars
slackMsg = 'Current Home IP: ' + ip

if not sameIP:
    # Run Slack if data has changed
    sc = SlackClient(slackToken)
    sc.api_call("chat.postMessage", channel=slackChannel, text=slackMsg)
