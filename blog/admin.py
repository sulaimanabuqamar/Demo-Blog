from django.contrib import admin
from .models import User, Post

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'age', 'gender', 'password']
    search_fields = ['name', 'user_id']

class PostAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'creation_date', 'likes', 'content', 'author', 'title', 'edited']
    search_fields = ['player_fname', 'team_name', 'player_number']

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)