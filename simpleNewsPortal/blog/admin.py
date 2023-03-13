from django.contrib import admin
from .models import Post, Category, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content', 'author']

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", 'user', 'content', 'date_commented')


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
