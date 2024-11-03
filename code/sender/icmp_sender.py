from scapy.all import *

target_ip = "172.18.0.3" 

icmp_packet = IP(dst=target_ip, ttl=1) / ICMP()

send(icmp_packet, verbose = False)
