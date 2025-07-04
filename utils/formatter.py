def display_packet(src, dst, protocol, payload):
    print(f"\n[Packet Captured]")
    print(f"Source IP      : {src}")
    print(f"Destination IP : {dst}")
    print(f"Protocol       : {protocol}")
    print(f"Payload        : {payload[:50]!r}")  # Print first 50 bytes
