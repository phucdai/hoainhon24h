from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class HeadingAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on', 'hits', 'author', 'category')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Post, HeadingAdmin)


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'created_on', 'hits', 'author', 'category')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}
#
#
# admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'id')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)