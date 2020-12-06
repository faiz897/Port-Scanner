# SYN scan
# UDP scan
# COMPREHENSIVE scan

import nmap

scanner = nmap.PortScanner()

print("Welcome to our NMAP Port scanner!")
print("<--------------------------------------------------------------->")

ip_add = input("Enter the IP address you want to scan: ")
print("The IP address is: "+ip_add)
type(ip_add)

resp = input("""\nPlease enter the scan you want to perform
        1. SYN ACK scan
        2. UDP scan
        3. COMPREHENSIVE scan\n""")
print("You have selected scan:", resp)

if resp == '1':
    print("NMAP version:",scanner.nmap_version())
    scanner.scan(ip_add, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols())
    print("open Ports: ", scanner[ip_add]["tcp"].keys())
elif resp == '2':
    print("NMAP version:", scanner.nmap_version())
    scanner.scan(ip_add, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols())
    print("open Ports: ", scanner[ip_add]["udp"].keys())
elif resp == '3':
    print("NMAP version:", scanner.nmap_version())
    scanner.scan(ip_add, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP status:", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols())
    print("open Ports: ", scanner[ip_add]["tcp"].keys())
else:
    print("Invalid Option!")
