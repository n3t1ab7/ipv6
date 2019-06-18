#!/usr/bin/python
# -*- coding: UTF-8 -*- 

"""
__title__ = '取随机IPV6地址'
__author__ = 'hbo'
__date__ = '2019/05/11'
"""

import os,sys
import random
import time
import datetime
from IPy import IP
from pathlib import Path


"""
    随机生成IP地址
    生成文件        
    IPV6ADDR    IP地址
    MAXNUM      最大数
    fileFn      保存文件
"""

def create_cidr_random_ipv6(IPV6ADDR, MAXNUM,fileFn):
    if(os.path.exists(fileFn)):       #  只生成一次
        return;
    ipv6s = IP(IPV6ADDR)
    len = ipv6s.len()
    fp = open(fileFn, "a+")
    count = 0
    while (count < MAXNUM):                                  #   随机取10000个地址，做解析用写配置文件，绑定网卡
        count = count + 1
        pos = random.randint(3,len)
        #ip_context = ipv6s[pos].strNormal() + '/64 '        #不换行    写配置文件用
        ip_context = ipv6s[pos].strNormal() + '/64\n'      #换行
        print(ip_context)
        fp.writelines(ip_context) 
    fp.close()
  
  


def runtimetest():
    """
        运行时间
    """
    starttime = time.time()
    #long running
    time.sleep(10)
    endtime = time.time()
    print (endtime - starttime)



def execCmd(cmd):  
    r = os.popen(cmd)  
    text = r.read()  
    r.close()  
    return text  


"""
注意  有些服务器网卡接口不一致，不一定是eth0
需要修改
"""
def add_ipv6_addr(addr):
    cmd="ifconfig eth0 inet6 add "+ addr;
    os.system(cmd)
    time.sleep(0.05)
    return cmd;




def bind_ipv6_eth(ipv6_addr_fn):
    """
    0.1秒则代表休眠100毫秒。 
    ipv6_addr_fn    生成的文件 10000 ip地址
    """
    file = open(ipv6_addr_fn)             # 返回一个文件对象
    while 1:
        addr = file.readline()
        if not addr:
            break
        pass 
        add_ipv6_addr(addr)

"""
获取本地已经绑定的IPV6信息

"""
def get_local_ipv6():
    cmd="ip -6 address show | grep inet6 | awk '{print $2}' | grep 2604  "
#    os.system(cmd)
    addr=execCmd(cmd)
    return addr

"""
ip -6 address show | grep inet6 | awk '{print $2}' | grep 2604  > locate-ipv6.txt
addr_num=`cat ipv6_addr.txt | wc -l`
sys_addr_ipv6=`cat locate-ipv6.txt | wc -l`
先获取本地已经绑定的IPV6地址
在判断是否与生成列表 的地址  有差异
"""
def check_bind_info(ipv6_addr_fn):
    cmd="ip -6 address show | grep inet6 | awk '{print $2}' | grep 2604 | wc -l"
    local_addr_num = execCmd(cmd)
    print(local_addr_num)


def main():
    starttime = time.time()

    IPV6ADDR="2604:d180:4a9:9e1::/64"
    MAXNUM=10000
    ipv6_addr_fn="ipv6_addr.txt"    
    create_cidr_random_ipv6(IPV6ADDR,MAXNUM,ipv6_addr_fn)     # 生成10000个IPV6地址
    my_file = Path(ipv6_addr_fn)
    if my_file.exists():
        bind_ipv6_eth(ipv6_addr_fn)

    endtime = time.time()
    print (endtime - starttime)


if __name__ == '__main__':
    main()



