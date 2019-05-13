#!/bin/bash

cd /home/ipv6

add_ipv6_fun(){
    
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
}

ip -6 address show | grep inet6 | awk '{print $2}' | grep 2604  > locate-ipv6.txt

addr_num=`cat ipv6_addr.txt | wc -l`

sys_addr_ipv6=`cat locate-ipv6.txt | wc -l`

if [ $sys_addr_ipv6 -gt $addr_num ]; 
then   
    echo "add IPV6 sucss"
else
    add_ipv6_fun
fi


date +%Y%m%d%H%M%S >> run.log




