from django.contrib.auth.models import User
from django.db import models


class AuditEvent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    who = models.ForeignKey(User)
    what = models.CharField(max_length=255)
    payload = models.TextField()

    def __str__(self):
        return u"{} - {}".format(self.created, self.what)
