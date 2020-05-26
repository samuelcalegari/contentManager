# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='Nom Utilisateur')
    firstname = models.CharField(max_length=50, verbose_name='Prénom')
    lastname = models.CharField(max_length=50, verbose_name='Nom')
    kind = models.CharField(max_length=1, verbose_name='Genre')
    yearofbirth = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'users'
        verbose_name = 'Utilisateur'

    def __str__(self):
        return self.lastname + ' ' + self.firstname

class Video(models.Model):
    name = models.CharField(max_length=50, verbose_name='Titre')
    tags = models.TextField(blank=True, null=True, verbose_name='Tags')
    category = models.CharField(max_length=50, blank=True, null=True, verbose_name='Catégorie')
    lang = models.CharField(max_length=2, blank=True, null=True, verbose_name='Langue')
    width = models.IntegerField(blank=True, null=True, verbose_name='Largeur')
    height = models.IntegerField(blank=True, null=True, verbose_name='Hauteur')
    length = models.CharField(max_length=50, blank=True, null=True, verbose_name='Durée')
    nbpeakers = models.IntegerField(blank=True, null=True, verbose_name='Nb. Intervenants')
    kindspeakers = models.CharField(max_length=1, blank=True, null=True, verbose_name='Genre')
    type = models.CharField(max_length=35, blank=True, null=True, verbose_name='Type')
    content = models.TextField()

    class Meta:
        managed = True
        db_table = 'videos'
        verbose_name = 'Vidéo'

    def __str__(self):
        return self.name

class Videoread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Utilisateur')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, verbose_name='Vidéo')

    class Meta:
        managed = True
        db_table = 'videosread'
        verbose_name = 'Visionages Vidéo'

    def __str__(self):
        return  str(self.user) + ' / ' + str(self.video)

class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name='Titre')
    tags = models.TextField(blank=True, null=True, verbose_name='Tags')
    category = models.CharField(max_length=200, blank=True, null=True, verbose_name='Catégorie')
    content = models.TextField(verbose_name='Contenu')

    class Meta:
        managed = True
        db_table = 'courses'
        verbose_name = 'Cour'

    def __str__(self):
        return self.name

class Courseread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Utilisateur')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, verbose_name='Cours')

    class Meta:
        managed = True
        db_table = 'coursesread'
        verbose_name = 'Inscription'

    def __str__(self):
        return  str(self.user) + ' / ' + str(self.course)