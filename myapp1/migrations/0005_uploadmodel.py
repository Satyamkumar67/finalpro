# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0004_auto_20170720_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to=b'user_images')),
                ('image_url', models.CharField(max_length=255)),
                ('points', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.UserModel')),
            ],
        ),
    ]
