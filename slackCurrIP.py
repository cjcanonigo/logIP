#!/usr/local/bin/python3

import subprocess
import datetime as dt
from slackclient import SlackClient
import sys
import os

# Run IP Command
cmd = ['dig', '@resolver1.opendns.com', 'ANY', 'myip.opendns.com', '+short']
result = subprocess.run(cmd, stdout=subprocess.PIPE)
ip = result.stdout.decode('utf-8')

# Set Credentials
if len(sys.argv) >= 1:
    slackToken = sys.argv[1]
    slackChannel = 'test_bmo'

# Set msg base
slackMsg = 'Current Home IP: ' + ip

# Run Slack if data has changed
sc = SlackClient(slackToken)
sc.api_call("chat.postMessage", channel=slackChannel, text=slackMsg)
