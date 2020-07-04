from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Timeplan(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 用户给出的数据
    title = models.CharField(max_length=100,default="title")
    describe = models.TextField()
    differ = models.IntegerField(default=0)
    num = models.IntegerField(default=1)
    complete = models.BooleanField(default=False)
    start = models.DateTimeField(default=timezone.now,blank=True,null=True)
    finish = models.DateTimeField(default=None,blank=True,null=True)
    # 计算出的数据
    time = models.IntegerField(default=0,blank=True)
    result = models.IntegerField(default=0,blank=True)
    gb4 = models.CharField(max_length=1000,blank=True)
    # 其他数据
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

class Template(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 用户给出的数据
    ttitle = models.CharField(max_length=100,default="title")
    tdescribe = models.TextField()
    tdiffer = models.IntegerField(default=0)
    tnum = models.IntegerField(default=1)
    # 其他数据
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.ttitle