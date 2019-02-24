#!/usr/local/bin/python3

import subprocess
import datetime as dt
from slackclient import SlackClient
import sys
import os

# Log Vars
currIP = 'currIP.txt'

# Set Credentials
if len(sys.argv) >= 1:
    slackToken = sys.argv[1]
    slackChannel = 'test_bmo'


# Set msg base
slackMsg = 'Current Home IP: '

# Check if IP changed
with open(currIP, 'r+') as f:
    slackMsg += f.readline()

# Run Slack if data has changed
sc = SlackClient(slackToken)
sc.api_call("chat.postMessage", channel=slackChannel, text=slackMsg)
