# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', max_length=30, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Activate',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('detail', models.TextField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': '活动信息',
                'verbose_name_plural': '活动信息',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, default='0')),
                ('scor', models.CharField(max_length=20, default='0')),
                ('author', models.CharField(max_length=255, default='0')),
                ('price', models.CharField(max_length=255, default='0')),
                ('time', models.CharField(max_length=255, default='0')),
                ('publish', models.CharField(max_length=255, default='0')),
                ('person', models.CharField(max_length=244, default='0')),
                ('yizhe', models.CharField(max_length=255, default='0')),
                ('tag', models.CharField(max_length=255, default='0')),
                ('brief', models.TextField(default='0')),
                ('ISBN', models.CharField(max_length=255, default='0')),
                ('pic', models.FileField(verbose_name='封面', default='pic/hmbb.png', upload_to='pic/')),
            ],
            options={
                'verbose_name': '书籍信息',
                'verbose_name_plural': '书籍信息',
            },
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('is_collect', models.BooleanField(default=False)),
                ('book', models.ForeignKey(to='book.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('up_count', models.IntegerField(verbose_name='点赞数', default=0)),
                ('book', models.ForeignKey(to='book.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '评论信息',
                'verbose_name_plural': '评论信息',
            },
        ),
        migrations.CreateModel(
            name='Commetupdown',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=0)),
                ('is_up', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(to='book.Comment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '评论点赞',
                'verbose_name_plural': '评论点赞',
            },
        ),
        migrations.CreateModel(
            name='Inactivate',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('is_in', models.BooleanField(default=False)),
                ('activate', models.ForeignKey(to='book.Activate')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '参与活动',
                'verbose_name_plural': '参与活动',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('book', models.ForeignKey(to='book.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '打分',
                'verbose_name_plural': '打分',
            },
        ),
    ]
