# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobb_forum', '0002_auto_20151231_0716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created'], 'get_latest_by': 'created', 'verbose_name': 'Post', 'verbose_name_plural': 'Posts', 'permissions': (('can_archive_post', 'Can archive Post'),)},
        ),
        migrations.AddField(
            model_name='post',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='Archived'),
        ),
    ]
