#!/usr/bin/env python3
import socket
import sys
from concurrent.futures import ThreadPoolExecutor

# TARGET SETUP
target = "127.0.0.1" # Default local test
if len(sys.argv) > 1:
    target = sys.argv[1]

print(f"[*] Starting fast multithreaded scan on target: {target}")
print("[*] Scanning all ports (1-65535)... Please wait.\n")

def scan_port(port):
    """Attempts to connect to a single port. Prints if open."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # 1 second timeout per port
        
        # connect_ex returns 0 if the connection was successful
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Found open port: {port}")
        s.close()
    except Exception:
        pass # Ignore errors (like system interrupts) and keep going

def main():
    # ThreadPoolExecutor manages running multiple threads at once.
    # max_workers=200 means 200 ports are being checked at the exact same millisecond!
    with ThreadPoolExecutor(max_workers=200) as executor:
        # map automatically passes every port from 1 to 65535 into our scan_port function
        executor.map(scan_port, range(1, 65536))
    
    print("\n[*] Scan complete!")

if __name__ == "__main__":
    main()