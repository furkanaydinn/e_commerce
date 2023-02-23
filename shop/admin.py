from django.contrib import admin
from .models import Product,Category,Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields =  ('title',) 
    list_display =   ('title',) 
    list_filter =    ('title',)
    prepopulated_fields = {'slug':('title',)}


class ProductAdmin(admin.ModelAdmin):
    search_fields =  ('title','category','brand') 
    list_display =   ('title','category','brand','price','status') 
    list_filter =    ('category','brand','status')
    prepopulated_fields = {'slug':('title',)}
   
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
