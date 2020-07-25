from django.contrib import admin

from .models import Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image')


admin.site.register(Post, AuthorAdmin)
