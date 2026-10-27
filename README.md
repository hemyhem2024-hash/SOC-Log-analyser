# SOC Log Analyzer - Brute Force Detection

## Overview
As a SOC Analyst L1, I built this tool to automate detection of brute-force attacks from Linux authentication logs. This simulates real SOC monitoring.

## Problem It Solves
Manual log review is slow. Attackers try many passwords - this script finds them in seconds.

## Features
- Parses /var/log/auth.log
- Extracts attacker IPs with regex
- Counts failed attempts per IP
- Flags IPs with >3 fails as BLOCK
- Maps to MITRE ATT&CK T1110

## Tools & Techniques
- Python 3, Regex, Collections
- Linux Logs, SIEM logic
- Threat Hunting mindset

## How To Run
1. Clone repo
2. Add your auth.log as sample.log
3. Run: python3 analyzer.py

## Sample Output
[!] Potential Brute-Force Detected: 6 failed attempts
Top attacker IPs:
    - 192.168.1.100 : 5 attempts -> BLOCK RECOMMEND
    - 45.33.12.5 : 1 attempts

## What I Learned
How SOC teams write detection rules similar to Splunk SPL and Wazuh rules for brute-force.

## Future Improvement
- Auto-block IP with iptables
- Send alert to Wazuh / Splunk
- Add email alerting

Author: Hemy | SOC Analyst | Eldoret, Kenya
