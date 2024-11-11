from django.contrib import admin
from articles.models import Post
from comments.models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created_at')
	list_filter = ('author', 'created_at')
	search_fields = ('title', 'author')
	ordering = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'post', 'created_at')
	list_filter = ('author', )
	search_fields = ('author', 'post')
	ordering = ('created_at',)
