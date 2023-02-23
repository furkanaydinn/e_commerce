from django.contrib import admin
from .models import Contact,Clients,Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    search_fields =  ('name','surname','job') 
    list_display =   ('name','surname','job') 
    list_filter =    ('name','surname','job')
   
    
class ClientAdmin(admin.ModelAdmin):
    search_fields =  ('client_name',) 
    list_display = ('client_name',) 
    list_filter = ('client_name',) 

class ContactAdmin(admin.ModelAdmin):
    search_fields =  ('name','email') 
    list_display = ('name','email') 
    list_filter = ('name','email') 

admin.site.register(Team,TeamAdmin)
admin.site.register(Clients,ClientAdmin)
admin.site.register(Contact,ContactAdmin)
# Register your models here.

