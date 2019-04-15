from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nid = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="0")
    scor = models.CharField(max_length=20, default="0")
    author = models.CharField(max_length=255, default="0")
    price = models.CharField(max_length=255, default="0")
    time = models.CharField(max_length=255, default="0")
    publish = models.CharField(max_length=255, default="0")
    person = models.CharField(max_length=244, default="0")
    yizhe = models.CharField(max_length=255, default="0")
    tag = models.CharField(max_length=255, default="0")
    brief = models.TextField(default="0")
    huojiang = models.CharField(default="无",max_length=255)
    is_huojiang = models.BooleanField(default=False)
    ISBN = models.CharField(max_length=255, default="0")
    pic = models.FileField(upload_to="pic/", default="pic/hmbb.png", verbose_name="封面")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书籍信息"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    nid = models.AutoField(primary_key=True)
    book = models.ForeignKey(to='Book', to_field='nid')
    user = models.ForeignKey(to='User', to_field='nid')
    content = models.TextField()
    up_count = models.IntegerField(verbose_name="点赞数", default=0)

    def __str__(self):
        return "{0}-{1}".format(self.nid,self.user)

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

class ScoreBook(models.Model):
    nid = models.AutoField(primary_key=True)
    book = models.ForeignKey(to='Book', to_field='nid')
    user = models.ForeignKey(to='User', to_field='nid')
    score = models.IntegerField()
    def __str__(self):
        return "{0}-{1}-{2}".format(self.user.username,self.book.title,self.score)

    class Meta:
        verbose_name = '用户评分'
        verbose_name_plural = verbose_name

class Score(models.Model):
    nid = models.AutoField(primary_key=True)
    book = models.ForeignKey(to='Book', to_field='nid')
    user = models.ForeignKey(to='User', to_field='nid')
    score = models.IntegerField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.user.username,self.book.title,self.score)
    class Meta:
        verbose_name = "打分"
        verbose_name_plural = verbose_name

class  Collect(models.Model):
    nid = models.AutoField(primary_key=True)
    book = models.ForeignKey(to='Book', to_field='nid')
    user = models.ForeignKey(to='User', to_field='nid')
    is_collect = models.BooleanField(default=False)
    def __str__(self):
        return "{0}收藏:{1}".format(self.user.username,self.book.title)
    class Meta:
        verbose_name = "收藏"
        verbose_name_plural = verbose_name

class Commetupdown(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to='User', to_field='nid')
    comment = models.ForeignKey(to='Comment', to_field='nid')
    count = models.IntegerField(default=0)
    is_up = models.BooleanField(default=False)

    class Meta:
        verbose_name = '评论点赞'
        verbose_name_plural = verbose_name




class Activate(models.Model):
    nid = models.AutoField(primary_key=True)
    detail = models.TextField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '活动信息'
        verbose_name_plural = verbose_name


class Inactivate(models.Model):
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to='User', to_field='nid')
    activate = models.ForeignKey(to='Activate', to_field='nid')
    is_in = models.BooleanField(default=False)

    def __str__(self):
        return "{0}-{1}".format(self.user.username,self.activate.name)

    class Meta:
        verbose_name = '参与活动'
        verbose_name_plural = verbose_name
