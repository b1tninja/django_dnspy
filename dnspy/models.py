# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.

from __future__ import unicode_literals

from django.db import models

class Name(models.Model):
    id = models.BigIntegerField(primary_key=True)
    parent = models.ForeignKey('Name', blank=True, null=True, db_column='parent', related_name='+')
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'name'

    def canonical_name(self):
        labels = [self.name]
        parent = self.parent
        while parent is not None:
            labels.append(parent.name)
            parent = parent.parent
        return '.'.join(labels)

    def __str__(self):
        return self.canonical_name()


class Packet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    source_address = models.BinaryField(blank=True, null=True, db_column='source')
    source_port = models.PositiveSmallIntegerField()
    destination_address = models.BinaryField(blank=True, null=True, db_column='destination')
    destination_port = models.PositiveSmallIntegerField()
    txnid = models.IntegerField()
    qr = models.BooleanField()
    opcode = models.PositiveSmallIntegerField()
    aa = models.BooleanField()
    tc = models.BooleanField()
    rd = models.BooleanField()
    z = models.PositiveSmallIntegerField()
    rcode = models.PositiveSmallIntegerField()
    qdcount = models.PositiveIntegerField()
    ancount = models.PositiveIntegerField()
    nscount = models.PositiveIntegerField()
    arcount = models.PositiveIntegerField()
    suffix = models.BinaryField(blank=True, null=True)
    questionset = models.BinaryField()
    recordset = models.BinaryField()
    effective_ttl = models.PositiveIntegerField()
    cached = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packet'


class ResourceHeader(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.ForeignKey(Name, db_column='name')
    qtype = models.IntegerField(db_column='type')
    qclass = models.IntegerField(db_column='class')

    class Meta:
        managed = False
        db_table = 'resource_header'

    def __str__(self):
        return "%s %s %s" % (self.name, self.type, self.qclass)


class ResourceRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    resource_header = models.ForeignKey(ResourceHeader, db_column='header')
    rdata = models.BinaryField(blank=True)

    class Meta:
        managed = False
        db_table = 'resource_record'

    def __str__(self):
        return "ResourceRecord<%s: %s>" % (self.resource_header, self.rdata)


class PacketQuestion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    packet = models.ForeignKey(Packet, db_column='packet')
    resource_header = models.ForeignKey(ResourceHeader, related_name='+')
    compressed_name = models.BinaryField(blank=True,null=True)

    class Meta:
        managed = False
        db_table = 'packet_question'

class PacketRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    packet = models.ForeignKey(Packet, db_column='packet')
    record = models.ForeignKey(ResourceRecord, db_column='record')
    compressed_name = models.BinaryField(blank=True, null=True)
    compressed_rdata = models.BinaryField(blank=True, null=True)
    ttl = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'packet_record'


class Query(models.Model):
    packet = models.OneToOneField(Packet, db_column='packet', primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, db_column='parent')
    nameserver = models.ForeignKey(ResourceRecord, db_column='nameserver', related_name='+')
    address = models.ForeignKey(ResourceRecord, db_column='address', related_name='+')
    response = models.ForeignKey(Packet, db_column='response', related_name='+')

    class Meta:
        managed = False
        db_table = 'query'


class Blacklist(models.Model):
    ip = models.BinaryField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'blacklist'