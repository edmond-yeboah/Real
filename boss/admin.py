from django.contrib import admin

# Register your models here.
from .models import agent, listing, compare, favourite, Message, region, compare_region, PrivateSchools, PublicSchools,Bank, Hospital,Manufacturing,Insurance,branch, SecondarySchools,Programs,product,Campuses, Facilities, Associations,service,facility

admin.site.register(agent)
admin.site.register(listing)
admin.site.register(compare)
admin.site.register(favourite)
admin.site.register(Message)
admin.site.register(region)
admin.site.register(compare_region)
admin.site.register(PrivateSchools)
admin.site.register(PublicSchools)
admin.site.register(Bank)
admin.site.register(Hospital)
admin.site.register(Manufacturing)
admin.site.register(Insurance)
admin.site.register(branch)
admin.site.register(Programs)
admin.site.register(product)
admin.site.register(Campuses)
admin.site.register(Facilities)
admin.site.register(Associations)
admin.site.register(SecondarySchools)
admin.site.register(service)
admin.site.register(facility)