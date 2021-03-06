#!/usr/bin/python
# Version 0.2

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
 
  def parselines(lines):
    for line in lines:
      mo = ipRegEx.search(line)
      ipHash.setdefault(mo.group(), 0)
      ipHash[mo.group()] += 1

  # RegEx to match for IPs in the log file
  ipRegEx = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')

  # Empty hash to hold IP address count
  ipHash = {}

  # Test to check if log was provided as an argument or piped via STDIN.

  if len(sys.argv) == 2:
    logfile = open(sys.argv[1])
    parselines(logfile.readlines())
  else:
    parselines(sys.stdin.readlines())
  
  # Sort and print formatted

  sortIpHash = sorted(ipHash, key=ipHash.__getitem__, reverse=True)
  for ip in sortIpHash:
    print(ip + ': ' + str(ipHash[ip]))
