# Generated by Django 3.0.6 on 2020-05-18 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20200507_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tags', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'courses',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': True},
        ),
        migrations.CreateModel(
            name='Courseread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.User')),
            ],
            options={
                'db_table': 'coursesread',
                'managed': True,
            },
        ),
    ]
