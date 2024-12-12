from django.contrib import admin

# Register your models here.



from django.contrib import admin
from .models import Invoice

# Kiểm tra model không được đăng ký nhiều lần
if not admin.site.is_registered(Invoice):
    admin.site.register(Invoice)
