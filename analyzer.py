#!/usr/bin/env python3
"""
SOC Log Analyzer - Brute Force Detection
Author: Collins | SOC Analyst Project
Detects brute-force attacks from Linux auth logs
"""

import re
from collections import Counter

LOG_FILE = "sample.log"
THRESHOLD = 5

# Regex to extract failed SSH attempts
FAILED_PATTERN = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

def analyze_logs():
    print("[+] SOC Log Analyzer Starting...")
    print(f"[+] Reading {LOG_FILE}\n")
    
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.read()
    except FileNotFoundError:
        print(f"[-] Error: {LOG_FILE} not found!")
        return

    ips = re.findall(FAILED_PATTERN, logs)
    
    if not ips:
        print("[+] No brute-force attempts found - System Clean")
        return

    counter = Counter(ips)
    
    print("="*50)
    print("BRUTE FORCE DETECTION REPORT")
    print("="*50)
    
    for ip, count in counter.items():
        status = "BLOCK RECOMMENDED" if count >= THRESHOLD else "Monitor"
        print(f"Attacker IP: {ip} : {count} attempts -> {status}")
    
    print("\n[+] Analysis Complete")
    print(f"[+] Total suspicious IPs: {len(counter)}")
    print("\n[SOC Action]: Block IPs with >5 attempts in firewall")

if __name__ == "__main__":
    analyze_logs()
