from django.contrib import admin

from .models import BlogLike, BlogPost

admin.site.register(BlogPost)
admin.site.register(BlogLike)
