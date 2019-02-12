# logIP

## Purpose

To check for IP changes (on a home network).

This will create 2 files, a currIP.txt and a histIP.txt.

currIP.txt will keep a single row containing the IPv4 external address of the current network.
histIP.txt will keep a history of timestamps + IPv4 based on whenever the script is run.

Lastly, it will connect to an authorized slack channel via OAuth token and send a message if the IP has changed.
