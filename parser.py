from scapy.layers.inet import IP, TCP, UDP, ICMP
from utils.formatter import display_packet

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        payload = bytes(packet[IP].payload)

        protocol = {6: 'TCP', 17: 'UDP', 1: 'ICMP'}.get(proto, str(proto))
        display_packet(src_ip, dst_ip, protocol, payload)
