from django.contrib import admin

# Register your models here.
from dnspy.models import Name, ResourceHeader, ResourceRecord, Packet, PacketQuestion, PacketRecord, Blacklist, Query

admin.site.register(Name)
admin.site.register(ResourceHeader)
admin.site.register(ResourceRecord)
admin.site.register(Query)
admin.site.register(Packet)
admin.site.register(PacketQuestion)
admin.site.register(PacketRecord)
admin.site.register(Blacklist)

