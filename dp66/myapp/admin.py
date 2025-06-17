from django.contrib import admin
from .models import Page,Post,Song

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name','rel_date','user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_name','rel_date','user']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name','song_dur','singers']