from django.db import models


class LogEntry(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    accept_language = models.CharField(max_length=255)

    def __str__(self):
        return f'Request ID: {self.id}'
