# Generated by Django 3.0.6 on 2020-05-07 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20200507_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='videoread',
            options={'managed': True},
        ),
    ]
