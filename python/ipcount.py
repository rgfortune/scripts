#!/usr/bin/python
# Version 0.1

# This script parses an Apache access log file and produces a list of the IPs with the most requests.

# Usage:
#   ipcount.py /path/to/log/file
#
#   If you want to filter by time you could pipe stdout into ipcount.py
#   egrep "(0|1)[0-9]/[A-Z][a-z]{2}/2015:13:4[0-7]" /path/to/log/file | ipcount.py 

import re, sys

# Read in log file
logfile = open(sys.argv[1])

# RegEx to match for IPs in the log file
ipRegEx = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')


# Iterate through the log, line by line, and keep running count of IPs
ipHash = {}
for line in logfile.readlines():
  mo = ipRegEx.search(line)
  ipHash.setdefault(mo.group(), 0)
  ipHash[mo.group()] += 1
  
# Sort and print formatted

sortIpHash = sorted(ipHash, key=ipHash.__getitem__, reverse=True)
for ip in sortIpHash:
  print(ip + ': ' + str(ipHash[ip]))
