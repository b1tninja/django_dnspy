__author__ = 'b1tninja'

from django import template
register = template.Library()

from DNSpy.enums import DnsQClass, DnsRClass, DnsQType, DnsRType

@register.filter
def rtype(x):
    return str(DnsRType(x))

@register.filter
def qtype(x):
    return str(DnsQType(x))

@register.filter
def rclass(x):
    return str(DnsRClass(x))

@register.filter
def qclass(x):
    return str(DnsQClass(x))