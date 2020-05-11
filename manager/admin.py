from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(Video)
admin.site.register(User)
admin.site.register(Videoread)