#!/bin/bash

ipv6_addr_fn="ipv6_addr.txt"

for ipaddr in `cat $ipv6_addr_fn`
do
    addr=`ip a | grep inet6 | grep $ipaddr`
    if [ -z "$addr" ]
    then
        echo $ipaddr
        ifconfig eth0 inet6 add $ipaddr
        usleep 100      #毫秒级别的sleep
    fi
done





















