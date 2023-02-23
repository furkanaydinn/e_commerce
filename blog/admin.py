from django.contrib import admin
from .models import Blog, BlogComment

# Register your models here.

class CommentItemLines(admin.TabularInline):
    model = BlogComment
    raw_id_fields = ['post']

class BlogAdmin(admin.ModelAdmin):
    search_fields =  ['title','author_name'] 
    list_display = ['title','slug','author_name','created_at','status']
    list_filter = ['author_name','created_at','status']
    inlines = [CommentItemLines]
    prepopulated_fields = {'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','post']

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment,CommentAdmin)