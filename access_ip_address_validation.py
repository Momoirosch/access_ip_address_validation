#!/usr/bin/env python3

# These are examples for valid and invalid inputs to your validation function
IPv4_STRING = "127.0.0.1"
IPv4_INVALID_STRING = "300.0.0.1"
IPv6_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
IPv6_INVALID_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334"
INVALID_IP_STRING = "Some arbitrary string"


def is_valid_IPv4_octet(octet: str):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""

    if len(octet) < 4:
        try:
            int(octet)
            if int(octet) < 256:
                return True
            return False
        except:
            return False
    return False

def is_valid_IPv4(ip: str):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""

    #check if ip is valid and split into octets
    if ip.count(".") == 3:
        octets = ip.split(".")
        valid_octet = 0
        # check if all octets are valid
        for octet in octets:
            if is_valid_IPv4_octet(octet):
                valid_octet += 1
                if valid_octet == 4:
                    return True
            else:
                return False
    return False

def is_valid_IPv6_hextet(hextet: str):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""

    if len(hextet) < 5:
        try:
            int(hextet, 16)
            if int(hextet, 16) < 65536:
                return True
            return False
        except:
            return False
    return False

def is_valid_IPv6(ip: str):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""

    if ip.count(":") == 7:
        hextets = ip.split(":")
        valid_hextet = 0
        # check if all hextets are valid
        for hextet in hextets:
            if is_valid_IPv6_hextet(hextet):
                valid_hextet += 1
                if valid_hextet == 8:
                    return True
            else:
                return False
    return False

def is_valid_IP(ip: str):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""

    if is_valid_IPv4(ip):
        return True
    elif is_valid_IPv6(ip):
        return True
    return False


# The following lines call is_valid_IP and print the result.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(
    f"{IPv4_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_STRING))
print(
    f"{IPv4_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_INVALID_STRING),
)
print(
    f"{IPv6_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_STRING))
print(
    f"{IPv6_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_INVALID_STRING),
)
print(
    f"{INVALID_IP_STRING} is a valid IP Address:",
    is_valid_IP(INVALID_IP_STRING),
)
