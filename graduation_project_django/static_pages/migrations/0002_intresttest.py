# Generated by Django 4.1.7 on 2023-04-20 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('static_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='intrestTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, max_length=200)),
                ('strongly_dislike', models.BooleanField(blank=True)),
                ('dislike', models.BooleanField(blank=True)),
                ('unsure', models.BooleanField(blank=True)),
                ('like', models.BooleanField(blank=True)),
                ('strongly_like', models.BooleanField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]