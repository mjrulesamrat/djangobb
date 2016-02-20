# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobb_forum', '0003_auto_20160120_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_moderated',
            field=models.BooleanField(default=False, verbose_name='Moderated'),
        ),
        migrations.AddField(
            model_name='topic',
            name='is_moderated',
            field=models.BooleanField(default=False, verbose_name='Moderated'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='theme',
            field=models.CharField(default='default', max_length=80, verbose_name='Theme', choices=[('punBB', 'punBB'), ('phpBB', 'phpBB'), ('IPB', 'IPB'), ('DjangoBB', 'DjangoBB'), ('default', 'default')]),
        ),
    ]
