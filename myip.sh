# /bin/sh

/sbin/ifconfig em1 | grep 'netmask' | awk '{print $2}'> ~/desktop_ip.txt
rsync -e ssh ~/desktop_ip.txt zandolie.izahtrini.com:~/ 2> /dev/null

