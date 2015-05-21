__author__ = 'b1tninja'

from django import template
register = template.Library()

from DNSpy.enums import DnsQClass, DnsRClass, DnsQType, DnsRType

@register.filter
def rtype(x):
    try:
        return str(DnsRType(x))
    except ValueError:
        return "DnsRType.%d" % x

@register.filter
def qtype(x):
    try:
        return str(DnsQType(x))
    except ValueError:
        return "DnsQType.%d" % x

@register.filter
def rclass(x):
    try:
        return str(DnsRClass(x))
    except ValueError:
        return "DnsRClass.%d" % x

@register.filter
def qclass(x):
    try:
        return str(DnsQClass(x))
    except ValueError:
        return "DnsQClass.%d" % x

