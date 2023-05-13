# Generated by Django 4.1.7 on 2023-05-12 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(choices=[(0, 'Strongly Dislike'), (1, 'Dislike'), (2, 'Unsure'), (3, 'Like'), (4, 'Strongly Like')])),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation_name', models.CharField(max_length=50)),
                ('occupation_description', models.CharField(max_length=5000)),
                ('occupation_interest', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, max_length=200)),
                ('question_type', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_description', models.TextField()),
                ('occupation_skill', models.ManyToManyField(to='static_pages.occupation')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_location', models.CharField(blank=True, max_length=30)),
                ('student_college', models.CharField(blank=True, max_length=30)),
                ('student_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('student_interest', models.CharField(blank=True, max_length=50)),
                ('student_answer', models.ManyToManyField(through='static_pages.Answer', to='static_pages.question')),
                ('student_skill', models.ManyToManyField(to='static_pages.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='answered_by',
            field=models.ManyToManyField(through='static_pages.Answer', to='static_pages.student'),
        ),
        migrations.AddField(
            model_name='occupation',
            name='occupation_skill',
            field=models.ManyToManyField(to='static_pages.skill'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('skill_id', models.ManyToManyField(to='static_pages.skill')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='static_pages.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='static_pages.student'),
        ),
    ]
