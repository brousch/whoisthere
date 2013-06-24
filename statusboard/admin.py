from django.contrib import admin

from models import Status

class StatusAdmin(admin.ModelAdmin):
    list_display = ['msg']
admin.site.register(Status, StatusAdmin)
