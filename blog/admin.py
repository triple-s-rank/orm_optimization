from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = 'post', 'author'
    list_per_page = 20
    list_display = 'post', 'author', 'published_at'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = 'likes', 'author'
    list_per_page = 20


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
