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
    pk = models.BigIntegerField(primary_key=True)
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
    pk = models.BigIntegerField(primary_key=True)
    source_address = models.ForeignKey('SourceAddress', db_column='source_address', blank=True, null=True)
    source_port = models.IntegerField()
    id = models.IntegerField()
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
    cached = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packet'


class Query(models.Model):
    pk = models.BigIntegerField(primary_key=True)
    question = models.ForeignKey('Question', db_column='question')
    nameserver = models.ForeignKey('Record', db_column='nameserver')
    address = models.ForeignKey('Record', db_column='address')
    requested = models.DateTimeField()
    completed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'query'


class Question(models.Model):
    pk = models.BigIntegerField(primary_key=True)
    name = models.ForeignKey(Name, db_column='name')
    qtype = models.IntegerField()
    qclass = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'question'

    def __str__(self):
        return "%s %s %s" % (self.name, self.type, self.qclass)

class Record(models.Model):
    pk = models.BigIntegerField(primary_key=True)
    name = models.ForeignKey(Name, db_column='name')
    rtype = models.IntegerField()
    rclass = models.IntegerField()
    ttl = models.IntegerField()
    rdata = models.TextField(blank=True)
    packet = models.ForeignKey(Packet, db_column='packet', blank=True, null=True)
    section = models.CharField(max_length=2) # ENUM ( qd, an, ns, ar )
    cached = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'

    def __str__(self):
        return "%s %d %d %d" % (self.name,
                                 self.type,
                                 self.rclass,
                                 self.ttl)


class Response(models.Model):
    pk = models.BigIntegerField(primary_key=True)
    query = models.ForeignKey(Query, db_column='query')
    packet = models.ForeignKey(Packet, db_column='packet')

    class Meta:
        managed = False
        db_table = 'response'


class SourceAddress(models.Model):
    pk = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=1) # ENUM, ( 4, 6 )
    ip = models.GenericIPAddressField() # almost want to use a packed binary field...
    blacklisted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'source_address'
