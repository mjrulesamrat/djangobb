# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobb_forum', '0002_auto_20160216_0652'),
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
    ]
