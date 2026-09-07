# Multi-Threaded Python Port Scanner

A high-performance, multi-threaded network scanner built in Python. This utility utilizes safe multi-threading mechanisms to scan a target host for open TCP ports rapidly without overwhelming system resources.

##  Features
* **Multi-Threaded Execution:** Utilizes Python's `threading` module to scan multiple ports simultaneously.
* **System Safeguards:** Employs a `BoundedSemaphore` to cap simultaneous active connections to 100, preventing resource exhaustion or crash loops.
* **Dynamic Targets:** Accepts target hostnames or IP addresses dynamically via command-line arguments.
* **Graceful Lifecycle:** Uses thread joining (`t.join()`) to ensure the main program waits for all worker threads to complete before exiting.

##  Requirements
* Python 3.x
* Standard built-in modules (`socket`, `sys`, `threading`) — no external installations required.

##  How to Use

1. **Clone the repository:**
   ```bash
   git clone <paste-your-github-repo-url-here>
   cd "Port Scanner"
   ```

2. **Run a scan against a specific target IP or Hostname:**
   You must provide the target host as a command-line argument:
   ```bash
   python "port scanner.py" 127.0.0.1
   ```
   *(Note: Use quotation marks around the filename if your path contains spaces).*

##  Sample Output
```text
[*] Launching threads for ports 1-1024 on 127.0.0.1...
[+] Port 135 is OPEN
[+] Port 445 is OPEN
[*] Scan complete!
```

##  Project Evolution & Roadmap
* [x] Basic sequential port testing baseline.
* [x] Core multithreading migration.
* [x] Bounded thread limiting for local stability.
* [ ] Add dynamic port range selections via command-line flags (e.g., `-p 20-80`).
* [ ] Implement basic service banner grabbing to identify running software.
