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
        db_table = 'names'

    def canonical_name(self):
        labels = [self.name]
        parent = self.parent
        while parent is not None:
            labels.append(parent.name)
            parent = parent.parent
        return '.'.join(labels)

    def __str__(self):
        return self.canonical_name()

class Question(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.ForeignKey(Name, db_column='name')
    type = models.IntegerField()
    qclass = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'questions'


class Query(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.ForeignKey(Question, db_column='question')
    nameserver = models.ForeignKey('Record', db_column='nameserver', related_name='+') #TODO: +?
    address = models.ForeignKey('Record', db_column='address', related_name='+') #TODO: +?
    requested = models.DateTimeField()
    completed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queries'
        verbose_name_plural = "queries"

class Record(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.ForeignKey(Name, db_column='name')
    type = models.IntegerField()
    rclass = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    ttl = models.IntegerField()
    rdata = models.BinaryField(blank=True)
    query = models.ForeignKey(Query, db_column='query', blank=True, null=True)
    cached = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'records'
