from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_description = models.TextField()

    occupation_skill = models.ManyToManyField('Occupation')

    def __str__(self):
        return self.skill_name


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    skill_id = models.ManyToManyField(Skill)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_location = models.CharField(max_length=30, blank=True)
    student_college = models.CharField(max_length=30, blank=True)
    student_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birth_date = models.DateField(null=True, blank=True)

    # relationships
    student_interest = models.CharField(max_length=50, blank=True)

    student_skill = models.ManyToManyField(Skill)

    # student answers
    student_answer = models.ManyToManyField('Question', through='Answer')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        img = Image.open(self.student_image.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            img.save(self.student_image.path)  # Save it again and override the larger image


class Occupation(models.Model):
    occupation_name = models.CharField(max_length=50)
    occupation_description = models.CharField(max_length=5000)

    occupation_skill = models.ManyToManyField(Skill)
    occupation_interest = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.occupation_name


class Question(models.Model):
    question = models.TextField(max_length=200, blank=True)
    question_type = models.CharField(max_length=50, blank=True)
    answered_by = models.ManyToManyField(Student, through='Answer')

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer_choices = [
        (0, 'Strongly Dislike'),
        (1, 'Dislike'),
        (2, 'Unsure'),
        (3, 'Like'),
        (4, 'Strongly Like'),
    ]

    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(choices=answer_choices)
