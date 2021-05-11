#!/usr/bin/env python3

def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True
ipchk = input("Apply an IP address: ")
if validIP(ipchk):
    print( "the IP is valid")

else:
    print("IP address is not valid")

