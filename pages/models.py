from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Speed(models.Model):
    name = models.CharField(max_length=255, verbose_name="السرعة")
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="العميل")
    speed = models.ForeignKey(Speed, on_delete=models.SET_NULL, verbose_name="السرعة", null=True)
    def __str__(self):
        return self.user.username

class UserPaymentData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="العميل")
    speed = models.CharField(max_length=255, verbose_name="السرعة")
    comment = models.TextField(verbose_name="تعليق")
    pay_date = models.DateField()
    def __str__(self):
        return self.user.username

