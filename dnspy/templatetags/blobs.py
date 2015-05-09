__author__ = 'b1tninja'

from django import template
register = template.Library()

import binascii

import ipaddress

@register.filter
def ipaddr(blob):
    if blob:
        if len(blob) == 4:
            return ipaddress.IPv4Address(blob).exploded
        if len(blob) == 16:
            return ipaddress.IPv6Address(blob).exploded

    return None

@register.filter
def hexlify(blob):
    return binascii.hexlify(blob)