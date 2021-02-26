from django.contrib import admin

from news.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
