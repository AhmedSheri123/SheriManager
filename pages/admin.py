from django.contrib import admin
from .models import UserPaymentData, Speed, UserProfile
# Register your models here.

admin.site.register(UserPaymentData)
admin.site.register(Speed)
admin.site.register(UserProfile)