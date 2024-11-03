from scapy.all import *

def packet_receive(packet):
    if packet.haslayer(ICMP):
        if(packet[IP].ttl == 1):
            print("Received ICMP Packet:")
            packet.show()

sniff(filter="icmp", prn=packet_receive, store=0)
