#!/bin/sh
curl --fail 'https://launchpad.net/libvterm/+download' 2>/dev/null |grep 'release' |head -n1 |sed -e 's,^ *,,;s,^v,,;s, release.*,,'
