#!/bin/bash
echo -en "Content-type: text/html<br>\n\n"
echo -en "Bash cgi script works :)<br>\n\n"
echo -en "User-agent: $HTTP_USER_AGENT<br>\n\n"
/bin/env
