# Simple Python Port Scanner

A lightweight, synchronous network utility written in Python to scan a target host for open ports. This script serves as the starting baseline for exploring networking concepts before implementing multi-threaded optimizations.

##  Features
* Automatically resolves local test targets (`127.0.0.1`).
* Supports custom target inputs via command-line arguments.
* Iterates sequentially through standard system ports to verify active TCP connections.
* Built-in timeout handling to quickly bypass unresponsive connections.

##  Requirements
* Python 3.x
* Standard built-in modules (`socket`, `sys`) — no external dependencies required.

##  How to Use

1. **Clone the repository or download the script:**
   ```bash
   git clone <paste-your-github-repo-url-here>
   cd <your-repo-folder-name>
   ```

2. **Run a default local scan (targets 127.0.0.1):**
   ```bash
   python Untitled-1.py
   ```

3. **Run a scan against a specific IP or Hostname:**
   ```bash
   python Untitled-1.py 192.168.1.1
   ```

##  Future Roadmap
* [ ] Implement **Multithreading** to significantly accelerate scanning speeds.
* [ ] Add custom port range inputs via command-line arguments.
* [ ] Export scan results to a log file (`.txt` or `.json`).

---
*Developed as a foundational networking experiment.*
