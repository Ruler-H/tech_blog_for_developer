from django.contrib import admin
from .models import Post, Category, Comment, Recomment, Image

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Recomment)
admin.site.register(Image)
