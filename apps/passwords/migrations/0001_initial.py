# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Time and Date Modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Time and Date Created')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Time and Date Modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Time and Date Created')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('username', models.CharField(blank=True, default=b'', max_length=200)),
                ('password', models.CharField(blank=True, default=b'', max_length=200)),
                ('notes', models.TextField(blank=True, default=b'')),
                ('host', models.CharField(blank=True, default=b'', max_length=200)),
                ('url', models.URLField(blank=True, default=b'')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='passwords.Category')),
                ('owned_by', models.ManyToManyField(blank=True, to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
