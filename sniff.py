from scapy.all import sniff, conf
from parser import process_packet

conf.use_pcap = True

def main():
    print("[*] Starting packet sniffer...")
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    main()