# Advanced Multi-Threaded Port Scanner & Banner Grabber

A high-performance network reconnaissance utility built in Python. This tool uses safe multi-threading mechanisms to scan a target host for open TCP ports rapidly, dynamically resolves domain names, and attempts to grab service banners to identify running applications.

##  Features
* **Multi-Threaded Execution:** Utilizes Python's `threading` module to scan multiple ports simultaneously.
* **System Safeguards:** Employs a `BoundedSemaphore` to cap simultaneous active connections to 100, preventing resource exhaustion, terminal freezing, or crash loops.
* **DNS Resolution:** Automatically resolves domain names/hostnames (e.g., `scanme.nmap.org`) to target IP addresses before starting the scan.
* **Service Banner Grabbing:** Attempts to read initial server responses (banners) on open ports to identify underlying software versions.
* **Graceful Lifecycle:** Uses thread joining (`t.join()`) to ensure the main program waits for all worker threads to finish before cleanly exiting.

##  Requirements
* Python 3.x
* Standard built-in modules (`socket`, `sys`, `threading`, `datetime`) — no external installations required.

##  How to Use

1. **Navigate to your project directory:**
   ```bash
   cd "Port Scanner"
   ```

2. **Run a scan against a specific target IP or Hostname:**
   You must provide the target host as a command-line argument in your terminal:
   ```bash
   python "port scanner.py" 127.0.0.1
   ```
   Or using a domain name:
   ```bash
   python "port scanner.py" scanme.nmap.org
   ```
   *(Note: Use quotation marks around the filename if your path contains spaces).*

##  Sample Output
```text
[*] Scan initiated on 127.0.0.1 at 2026-09-08 00:12:34.567890
[*] Checking ports 1-1024... Please wait.

[+] Port 135: OPEN (Standard response connection)
[+] Port 445: OPEN (Standard response connection)

[*] Scan complete!
```

##  Project Evolution & Roadmap
* [x] Basic sequential port testing baseline.
* [x] Core multithreading migration.
* [x] Bounded thread limiting for local stability.
* [x] DNS hostname resolution and target validation.
* [x] Service banner grabbing implementation.
* [ ] Add a file-writing feature to automatically save scan logs to a `.txt` file.
