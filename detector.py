# Nicholas Mauro  (nmauro@bu.edu)

import sys
import dpkt
import socket

SYN = []
SYN_ACK = []
f = open((sys.argv[1]), "rb")
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    try:
        eth = dpkt.ethernet.Ethernet(buf)
        if dpkt.ethernet.ETH_TYPE_IP == eth.type:
            ip = eth.data
            if dpkt.ip.IP_PROTO_TCP == ip.p:
                tcp = ip.data
                if tcp.flags == 2:
                    Source = socket.inet_ntoa(ip.src)
                    SYN.append(Source)
                if tcp.flags == 18:
                    Destination = socket.inet_ntoa(ip.dst)
                    SYN_ACK.append(Destination)
    except dpkt.dpkt.NeedData:
        continue
    except dpkt.dpkt.UnpackError:
        continue

while len(SYN) > 0:
    address = SYN[0]
    if SYN.count(address) >= 3*SYN_ACK.count(address):
        print address
    SYN = [i for i in SYN if i != address]

f.close()