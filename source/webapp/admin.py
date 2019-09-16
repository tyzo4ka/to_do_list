from django.contrib import admin
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'description', 'detailed', 'status', 'complete_before']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['description', 'detailed', 'status', 'complete_before']



admin.site.register(Task, TaskAdmin)

