#!/bin/bash

if [ -z $1 ]
then
	echo "Please specify a target host"
	exit -1
fi

HOST=$1

MAX_USERS=5
MAX_PAGES=15
MAX_DELAY=60

while true; do
	N_USERS=$(( ${RANDOM} % ${MAX_USERS} + 1 ))
	echo "Generating ${N_USERS} users"
	for i in $(seq ${N_USERS}); do
		N_PAGES=$(( ${RANDOM} % ${MAX_PAGES} + 1 ))
		echo "Crawling ${N_PAGES} pages"
		locust --no-web -c 1 -r 1 -n ${N_PAGES} -f $(dirname -- "$0")/locustfile.py --host http://${HOST} WebsiteUser >/dev/null 2>&1 &
	done
	DELAY=$(( ${RANDOM} % ${MAX_DELAY} ))
	echo "Sleeping ${DELAY} seconds"
	sleep ${DELAY}
done

