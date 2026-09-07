#!/usr/bin/env python3
import socket
import sys
import threading
from datetime import datetime

# FINAL VERSION: Added service banner grabbing to identify running applications.
# Updated with a safe Thread Limiter and Joins to prevent system crash loops.

# Limit simultaneous active connections to 100 so your system doesn't crash
thread_limiter = threading.BoundedSemaphore(100)

def scan_port(target_ip, port):
    thread_limiter.acquire()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            # Try to grab the banner safely
            try:
                # Optional: Send a generic request to trick certain servers into replying
                s.send(b"HEAD / HTTP/1.0\r\n\r\n") 
                banner = s.recv(512).decode().strip()
                if banner:
                    print(f"[+] Port {port}: OPEN --> {banner}")
                else:
                    print(f"[+] Port {port}: OPEN (No banner responded)")
            except:
                print(f"[+] Port {port}: OPEN (Standard response connection)")
        s.close()
    except Exception:
        pass
    finally:
        thread_limiter.release()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scanner.py <Target IP>")
        sys.exit(1)
        
    target = sys.argv[1]
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Verification failed: Could not resolve target hostname.")
        sys.exit(1)
        
    print(f"[*] Scan initiated on {target_ip} at {str(datetime.now())}")
    print("[*] Checking ports 1-1024... Please wait.\n")
    
    threads = []
    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    # Wait for all 1,024 threads to finish scanning before ending the script
    for t in threads:
        t.join()

    print("\n[*] Scan complete!")

if __name__ == "__main__":
    main()
