from django.contrib import admin
from .models import Project, ViewCount, Message

admin.site.register(Project)
admin.site.register(ViewCount)
admin.site.register(Message)

