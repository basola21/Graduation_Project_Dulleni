# Generated by Django 4.1.7 on 2023-03-27 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='password1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='students',
            name='password2',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
