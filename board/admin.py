from django.contrib import admin
from .models import Board_Post, Board_Image, Board_Comment, Board_Recomment

admin.site.register(Board_Post)
admin.site.register(Board_Image)
admin.site.register(Board_Comment)
admin.site.register(Board_Recomment)
