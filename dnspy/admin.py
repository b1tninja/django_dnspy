from django.contrib import admin

# Register your models here.
from dnspy.models import Name, Record, Query, Question

admin.site.register(Name)
admin.site.register(Record)
admin.site.register(Question)
admin.site.register(Query)
