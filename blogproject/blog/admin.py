from django.contrib import admin
from blog.models import *
# Register your models here.

admin.site.register(TagInfo)
admin.site.register(NoteInfo)
admin.site.register(CommentInfo)