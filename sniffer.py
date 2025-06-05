from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

packets = []

def process_packet(packet):
    if IP in packet:
        proto = 'TCP' if TCP in packet else 'UDP' if UDP in packet else 'Other'
        packets.append({
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'src': packet[IP].src,
            'dst': packet[IP].dst,
            'proto': proto,
            'payload': str(bytes(packet.payload))[:100]  # First 100 bytes only
        })

def start_sniffing(count=10):
    global packets
    packets = []
    sniff(filter="ip", prn=process_packet, count=count)
    return packets
