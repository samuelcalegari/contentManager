from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

# Utilisateurs
admin.site.register(User)

# Videos
admin.site.register(Video)

# Visionnages Videos
admin.site.register(Videoread)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

# Cours
admin.site.register(Course, CourseAdmin)

# Inscriptions
admin.site.register(Courseread)