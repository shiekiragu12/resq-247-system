from django.contrib import admin
from .models import AppConfig, Tag, Blog, Reply
# Register your models here.

admin.site.register([AppConfig, Tag, Blog, Reply])
