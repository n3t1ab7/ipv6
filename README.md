

随机生成的地址文件
ipv6_addr.txt

addr.sh  执行添加 绑定网卡

检查 已经绑定 IPV6 地址
ip -6 address show | grep inet6 | awk '{print $2}' | cut -d'/' -f1 | grep 2604  > locate-ipv6.txt

计算 a-b式 差集     获取没有绑定 成功 的IP地址
grep -F -v -f locate-ipv6.txt  ipv6_addr.txt | sort | uniq > diff-ipv6.txt


















