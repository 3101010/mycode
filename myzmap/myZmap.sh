#!/bin/bash
#author:Net
#version：v1.0
#date:2017-07-02

export sName=$1
export sNetwork=$2
export sPort1=$3
export sPort2=$4
export sPort3=$5
export sPort4=$6
export sPort5=$7
#test
ping 114.114.114.114 -c 1 -t 2 > nul

cat > /etc/zmap/zmap.conf <<EOF
### Probe Module to use
#probe-module tcp_synscan

### Destination port to scan
#target-port 135

### Scan rate in packets/sec
#rate 1000

### Scan rate in bandwidth (bits/sec)
#bandwidth 1M	# 1mbps


#output-fields "daddr,sport,seq,ack,in_cooldown,is_repeat,timestamp"
output-fields "saddr,sport,ttl,cooldown,repeat,timestamp-str,classification,success"
output-filter "success = 1 && cooldown = 0 && repeat = 0"
#output-filter "(success = 0 || success = 1) || (cooldown = 1 || cooldown = 0)"

#output-file=/tmp/zmap-result-10.41-135
##output module. use zmap --list-output-modules list support modules
## output-module=redis-csv
#
##output redis args. tcp://ip:port/queuename
## output-args=tcp://127.0.0.1:6379/zmap


### Blacklist file to use. We encourage you to exclude
### RFC1918, IANA reserved, and multicast networks,
### in addition to those who have opted out of your
### network scans.
blacklist-file "/etc/zmap/blacklist.conf"

### Optionally print a summary at the end
#summary
source-port 50000-60000
cooldown-time 15
seed 3
EOF

sleep 1

cat > /etc/zmap/blacklist.conf <<EOF

# From IANA IPv4 Special-Purpose Address Registry
# http://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
# Updated 2013-05-22

0.0.0.0/8           # RFC1122: "This host on this network"
#10.0.0.0/8          # RFC1918: Private-Use
100.64.0.0/10       # RFC6598: Shared Address Space
127.0.0.0/8         # RFC1122: Loopback
169.254.0.0/16      # RFC3927: Link Local
#172.16.0.0/12       # RFC1918: Private-Use
#192.0.0.0/24        # RFC6890: IETF Protocol Assignments
#192.0.2.0/24        # RFC5737: Documentation (TEST-NET-1)
#192.88.99.0/24      # RFC3068: 6to4 Relay Anycast
#192.168.0.0/16      # RFC1918: Private-Use
198.18.0.0/15       # RFC2544: Benchmarking
198.51.100.0/24     # RFC5737: Documentation (TEST-NET-2)
203.0.113.0/24      # RFC5737: Documentation (TEST-NET-3)
240.0.0.0/4         # RFC1112: Reserved
255.255.255.255/32  # RFC0919: Limited Broadcast

# From IANA Multicast Address Space Registry
# http://www.iana.org/assignments/multicast-addresses/multicast-addresses.xhtml
# Updated 2013-06-25

224.0.0.0/4         # RFC5771: Multicast/Reserved
EOF

sleep 1

if  [ $sPort1 ];
then
echo "Start scan port: $sPort1 !!!"
zmap -p $sPort1 -r 1000 -o "${sName}_Result_${sPort1}.csv" $sNetwork;
sleep 1;
fi
if  [ $sPort2 ];
then
echo "Start scan port: $sPort2!!!"
zmap -p $sPort2 -r 1000 -o "${sName}_Result_${sPort2}.csv" $sNetwork;
sleep 1;
fi
if  [ $sPort3 ];
then
start "Scan port: $sPort3!!!"
zmap -p $sPort3 -r 1000 -o "${sName}_Result_${sPort3}.csv" $sNetwork;
sleep 1;
fi
if  [ $sPort4 ];
then
ehco "Start scan port: $sPort4!!!"
zmap -p $sPort4 -r 1000 -o "${sName}_Result_${sPort4}.csv" $sNetwork;
sleep 1;
fi
if  [ $sPort5 ];
then
echo "Start scan port: $sPort5!!!"
zmap -p $sPort5 -r 1000 -o "${sName}_Result_${sPort5}.csv" $sNetwork;
sleep 1;

else
cut -d$'\n' -f2- ${sName}_Result_*.csv  > ${sName}_Result_SUM.csv;
#mv Result_SUM_000.csv ${sName}_Result_SUM.csv;
echo "Scan Ok!"
echo "Result is in ${sName}_Result_SUM.csv !!!"
fi