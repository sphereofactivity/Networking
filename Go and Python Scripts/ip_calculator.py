import ipaddress
import sys

"""
To do: 
- function to calculate CIDR
- function to calculate Network + Broadcast address
- function to calculate hostMin and hostMax address
- function to calculate available hosts
"""

def ipv4_to_bin(ip):
    """
    - the functionality is that the ip is passed to the function and converted to binary.
    - bin() takes an int so the ip is converted to an int and 0b is removed from the int and replaced with blank space
    - as we only need to read this to calculate the ip, it is converted to a string and a list is made to split and rejoin the string
    - iterate through the str in steps of 8
    - the iteration chunks are added to the bin_list + a "." for readability for 8 bits per octet
    - the final . is removed from the str and printed to the terminal
    """
    try:
        binary_ip = bin(int(ip)).replace("0b", "").zfill(32)
        str_bin_ip = str(binary_ip)
        bin_list = []
        for i in range(0, len(str_bin_ip), 8):
            bin_list.extend(str_bin_ip[i : i + 8])
            bin_list.append(".")
            string_subnet = "".join(bin_list)
            string_subnet = string_subnet[:-1]
        print(string_subnet)
    except ValueError:
        print("Invalid ip input")
    except TypeError:
        print("Error processing the ip address")


def main():
    # this needs to be updated to take an input instead of a hardcoded value
    # update once remaining functions are completed
    ip = ipaddress.ip_address("192.168.2.1")
    ipv4_to_bin(ip)
    sys.exit()

main()
