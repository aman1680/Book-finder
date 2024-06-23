from django.contrib import admin
from django.contrib.admin.sites import site

from .models import Repository

# Register your models here.

class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')

admin.site.register(Repository, RepositoryAdmin)
