from django.contrib import admin

from .models import (
            Post, Author, Tags
            )

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tags)
