# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    kind = models.CharField(max_length=1)
    yearofbirth = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return self.lastname + ' ' + self.firstname

class Video(models.Model):
    name = models.CharField(max_length=50)
    tags = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    lang = models.CharField(max_length=2, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    length = models.CharField(max_length=50, blank=True, null=True)
    nbpeakers = models.IntegerField(blank=True, null=True)
    kindspeakers = models.CharField(max_length=1, blank=True, null=True)
    type = models.CharField(max_length=35, blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = True
        db_table = 'videos'

    def __str__(self):
        return self.name

class Videoread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = 'videosread'

    def __str__(self):
        return  str(self.user) + ' / ' + str(self.video)

class Course(models.Model):
    name = models.CharField(max_length=200)
    tags = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = True
        db_table = 'courses'

    def __str__(self):
        return self.name

class Courseread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = 'coursesread'

    def __str__(self):
        return  str(self.user) + ' / ' + str(self.course)