# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_auto_20151126_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='content',
            new_name='name',
        ),
    ]
