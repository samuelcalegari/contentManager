# Generated by Django 3.0.6 on 2020-05-07 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20200507_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
        migrations.AddField(
            model_name='videoread',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.User'),
        ),
        migrations.AddField(
            model_name='videoread',
            name='videoid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Video'),
        ),
    ]
