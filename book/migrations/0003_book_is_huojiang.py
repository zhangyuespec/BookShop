# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_huojiang'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_huojiang',
            field=models.BooleanField(default=False),
        ),
    ]
