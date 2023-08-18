from django.contrib.auth.models import Group
from django_fields.fields import EncryptedTextField, EncryptedCharField
from django.db import models


class _AbstractModel(models.Model):
    class Meta:
        abstract = True

    modified = models.DateTimeField('Time and Date Modified', auto_now=True)
    created = models.DateTimeField('Time and Date Created', auto_now_add=True)


class CategoryManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Category(_AbstractModel):
    objects = CategoryManager()

    name = models.CharField(max_length=40, unique=True)

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Categories'


class PasswordManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Password(_AbstractModel):
    objects = PasswordManager()

    name = models.CharField(max_length=40, unique=True)
    username = models.CharField(max_length=200, blank=True, default='')
    password = EncryptedCharField(max_length=200, blank=True, default='')
    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, default='')
    host = models.CharField(max_length=200, blank=True, default='')
    url = models.URLField(blank=True, default='')
    owned_by = models.ManyToManyField(Group, blank=True)

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return unicode(self.name)

    def is_owned_by(self, user):
        """Detect if the user owns this Password by returning the queryset of
        groups the user is in that have ownership."""
        return self.owned_by.all() & user.groups.all()
