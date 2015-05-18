#!/usr/bin/python
# Version 0.1

# This script parses an Apache access log file and produces a list of the IPs with the most requests.
# 
#
# Usage:
#   $ ipcount.py /path/to/log/file
#
#   The script can also be used in a tool chain.
#
#   $ cat /path/to/log/file | ipcount.py  
#   $ egrep "(0|1)[0-9]/[A-Z][a-z]{2}/2015:13:4[0-7]" /path/to/log/file | ipcount.py 

import re, sys


if __name__=="__main__":

  # RegEx to match for IPs in the log file
  ipRegEx = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')

  # Empty hash to hold IP address count
  ipHash = {}

  # Test to check wheter log was provided as an argument or piped vis STDIN.
  # Iterate through the log, line by line, and keep running count of IPs

  if len(sys.argv) == 2:
    logfile = open(sys.argv[1])
    for line in logfile.readlines():
      mo = ipRegEx.search(line)
      ipHash.setdefault(mo.group(), 0)
      ipHash[mo.group()] += 1
  else:
    for line in sys.stdin.readlines():
      mo = ipRegEx.search(line)
      ipHash.setdefault(mo.group(), 0)
      ipHash[mo.group()] += 1
  
  # Sort and print formatted

  sortIpHash = sorted(ipHash, key=ipHash.__getitem__, reverse=True)
  for ip in sortIpHash:
    print(ip + ': ' + str(ipHash[ip]))
