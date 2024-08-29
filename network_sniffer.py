import pyshark
def sniffing(interface):
    print(f"[*] Starting packet sniffing on {interface}...")
    
    capture = pyshark.LiveCapture(interface=interface,tshark_path="f://programs//wireshark//tshark.exe")

    for packet in capture.sniff_continuously():
        try:
            
            if 'IP' in packet:
                
                ip_layer = packet['IP']
                print(f"Source: {ip_layer.src}, Destination: {ip_layer.dst}, Protocol: {ip_layer.proto}")
        except AttributeError as e:
            
            print(f"Packet error: {e}")
sniffing('wi-fi')
