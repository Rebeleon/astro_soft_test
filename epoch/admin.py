import os
from django.contrib import admin
from django.utils.html import format_html
from epoch.models import LogEntry
from astro_soft_test.settings import MEDIA_URL


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'ip_address', 'user_agent', 'get_accept_language_with_flag')

    def get_accept_language_with_flag(self, obj):
        image_filename = '{}.svg'.format(obj.accept_language[3:5])
        image_path = os.path.join(MEDIA_URL, 'flags', image_filename)
        return format_html('<img src="{}" alt="{}">', image_path, obj.accept_language[3:5])

    get_accept_language_with_flag.short_description = 'Accept Language'
