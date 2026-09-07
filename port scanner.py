#!/usr/bin/env python3
import socket
import sys

# STARTING POINT: Basic script to check if a port is open
# Dishant: Testing basic connection before adding threads later

target = "127.0.0.1" # default local test
if len(sys.argv) > 1:
    target = sys.argv[1]

print(f"[*] Starting basic scan on target: {target}")

# Loop through standard web and management ports
for port in [21, 22, 80, 443, 8080]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Found open port: {port}")
    s.close()
