#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Port Scanner
This script is intended for educational purposes only and was created as part of a CyberSec lab. 
Please use it responsibly.

This module provides functionality to perform a port scan on one or multiple target IP addresses. It 
includes capabilities to scan a range of ports on each target to identify open ports.The script allows 
for scanning multiple targets by accepting a comma-separated list of IP addresses. The user can specify 
the range of ports to scan for each target.

Functions:
- scan(target: str, ports: int): Initiates a port scan on the specified target for the given range of ports.
- scan_port(ipaddress: str, port: int): Scans a specific port on the given IP address and reports its status.

Usage:
Run the script and enter the targets and the number of ports to scan when prompted. The script will display the 
status of each port (open or closed) for each target IP address.

Note:
- The script requires the 'socket' and 'termcolor' modules.
- Port scanning can be illegal or considered hostile activity on certain networks. Ensure you have authorization
  before scanning ports on any network.

Example:
    $ python port_scanner.py
    [*] Enter Targets To Scan (split them by comma): 192.168.1.1, 192.168.1.2
    [*] Enter How Many Ports To Scan: 500
    [+] Port 22 open on 192.168.1.1
    [-] Port 80 closed on 192.168.1.2

"""

import socket
import termcolor


def scan(target: str, ports: int) -> None:
    """
    Perform a port scan on the specified target.

    Parameters
    ----------
    target : str
        The target IP address to scan.
    ports : int
        The number of ports to scan.

    Returns
    -------
    None

    """

    print(f"\n Starting Scan For {target}")
    try:
        for port in range(1, ports + 1):
            scan_port(target, port)
    except KeyboardInterrupt:
        print(termcolor.colored("\n[!] Scan interrupted by user. Exiting...", "red"))


def scan_port(ipaddress: str, port: int) -> None:
    """
    Scan a specific port on the given IP address.

    Parameters
    ----------
    ipaddress : str
        The target IP address.
    port : int
        The port number to scan.

    Returns
    -------
    None

    """

    try:
        sock = socket.socket()  # Initiate socket object
        sock.connect((ipaddress, port))
        print(termcolor.colored(f"[+] Port {port} open", "green"))
        socket.close()
    except:
        print(termcolor.colored(f"[-] Port {port} closed", "red"))


if __name__ == "__main__":
    targets = input("[*] Enter Targets To Scan (split them by comma): ")
    ports = int(input("[*] Enter How Many Ports To Scan: "))
    try:
        if "," in targets:
            print(termcolor.colored("[*] Scanning Multiple Targets", "green"))
            for ip_addr in targets.split(","):
                scan(ip_addr.strip(" "), ports)
        else:
            scan(targets, ports)
    except KeyboardInterrupt:
        print(termcolor.colored("\n[!] Scan interrupted by user. Exiting...", "red"))
