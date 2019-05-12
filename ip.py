#!/usr/bin/python
# -*- coding: UTF-8 -*- 

"""
__title__ = '取随机IPV6地址'
__author__ = 'sbkk'
__date__ = '2019/05/11'
"""

import os,sys
import random
from IPy import IP

IPV6ADDR = input("IPV6ADDR:")
#IPV6ADDR="2604:180:2:1334::/64"

if(os.path.exists("10000.txt")):
    os.remove("10000.txt")

ipv6s = IP(IPV6ADDR)
len = ipv6s.len()

# random.randint(0,99)
#   print(ipv6s.len())

ipv6_addr_fn="ipv6_addr.txt"


fp = open(ipv6_addr_fn, "a+")

count = 0
while (count < 10000):                                  #   随机取10000个地址，做解析用写配置文件，绑定网卡
    count = count + 1
    pos = random.randint(10,len)
    #ip_context = ipv6s[pos].strNormal() + '/64 '        #不换行    写配置文件用
    ip_context = ipv6s[pos].strNormal() + '/64\n'      #换行
    print(ip_context)
    fp.writelines(ip_context) 

fp.close()














