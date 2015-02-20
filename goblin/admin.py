from django.contrib import admin

# Register your models here.
from goblin.models import Project, Release, Change

admin.site.register(Project)
admin.site.register(Release)
admin.site.register(Change)
