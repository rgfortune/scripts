#!/usr/bin/python

# For CRON
# DISPLAY=:0 XAUTHORITY=/var/run/gdm/auth-for-ricardo-UINtTM/database /usr/bin/python /path/to/script.py

import urllib2
import pynotify
import re
import sys

pynotify.init('Basic')
message = pynotify.Notification('Phone Status', 'You need to login.')

def main():
  req = urllib2.Request('http://phoneboy.intra.rackspace.com/pb4-list.php?group=34')
  response = urllib2.urlopen(req)
  the_page = response.read()

  if re.search(r'Ricardo\sFortune[\s\n\w<>=":;%#/-]+OUT', the_page):
    message.show()
  else:
    sys.exit(0)

if __name__ == "__main__":
  main()
