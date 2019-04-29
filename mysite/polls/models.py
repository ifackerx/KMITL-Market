from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# users/models.py
from django.contrib.auth.models import AbstractUser



class Poll(models.Model):

    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    SINGLE = '01'
    MULTIPLE = '02'
    TYPES = (
        (SINGLE, 'Single answer'),
        (MULTIPLE, 'Multiple answer')
    )
    type = models.CharField(max_length=2, choices=TYPES, default='01')
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)

    def __str__(self):
        return '(%s) %s' % (self.poll.title, self.text)


class Choice(models.Model):
    text = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self):
        return '(%s) %s' % (self.question.text, self.text)


class Answer(models.Model):
    choice = models.OneToOneField(Choice, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

class Comment(models.Model):

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField()
    tel = models.CharField(max_length=10)

    def __str__(self):
        return self.title


# project

class ShopArea(models.Model):
    area_code = models.CharField(max_length=10)
    del_shop = models.BooleanField(default=False)


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_open = models.CharField(null=True, blank=True, max_length=100)
    shop_detail = models.CharField(null = True, blank=True, max_length=500)
    shop_area = models.ForeignKey(ShopArea, on_delete=models.PROTECT, default=1)
    shop_owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
class Review(models.Model):
    review_title = models.CharField(max_length=100)
    review_message = models.CharField(max_length=500)
    review_shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    review_user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    text = models.CharField(max_length=100, null=True)