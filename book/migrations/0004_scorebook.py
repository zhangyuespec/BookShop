# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_is_huojiang'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreBook',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('book', models.ForeignKey(to='book.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户评分',
                'verbose_name_plural': '用户评分',
            },
        ),
    ]
