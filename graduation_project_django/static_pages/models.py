from django.db import models
from django.contrib.auth.models import User

class skills(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_description = models.DateField()

    def __str__(self):
        return self.skill_name


class courses(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    skill_id = models.ManyToManyField(skills)

    def __str__(self):
        return self.course_name

class intrests(models.Model):
    intrest_name = models.CharField(max_length=50)
    intrest_description = models.CharField(max_length=50)

    def __str__(self):
        return self.intrest_name

class students(models.Model):
    student_name = models.OneToOneField(User, on_delete=models.CASCADE)
    studnet_location = models.CharField(max_length=30, blank=True)
    student_email = models.EmailField(max_length=500, blank=True)
    student_college = models.CharField(max_length=30, blank=True)
    student_image = models.ImageField(upload_to='images/', blank=True)
    birth_date = models.DateField(null=True, blank=True)

    student_intrest = models.ForeignKey(intrests, on_delete=models.SET_NULL, null = True)
    student_skill = models.ManyToManyField(skills)

    def __str__(self):
        return self.student_name


class occupations(models.Model):
    occupation_name = models.CharField(max_length=50)
    occupation_description = models.CharField(max_length=50)
    
    ocuupation_skill = models.ManyToManyField(skills)
    occupation_intrest = models.ForeignKey(intrests, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.occupation_name