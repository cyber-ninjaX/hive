from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class YubikeyAuth(models.Model):
    yubikey_id = models.CharField(max_length=12, unique=True, null=True)
    user_id = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=100, null=True)

    otp_disabled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user_name

    def make_user(self):
        user = User.objects.get(pk=self.user_id)
        name = user.first_name + ' ' + user.last_name
        if name == ' ':
            self.user_name = user.username
        else:
            self.user_name = name

    def save(self, *args, **kwargs):
        if not self.user_name:
            self.make_user()
        super(YubikeyAuth, self).save(*args, **kwargs)


class YubikeyAuthAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'created_at', 'updated_at', 'otp_disabled')
    search_fields = ('user_name',)


admin.site.register(YubikeyAuth, YubikeyAuthAdmin)
