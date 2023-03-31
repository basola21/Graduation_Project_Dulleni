from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# this is the skills model
class skills(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_description = models.TextField()

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studnet_location = models.CharField(max_length=30, blank=True)
    student_college = models.CharField(max_length=30, blank=True)
    student_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birth_date = models.DateField(null=True, blank=True)


    #relationships
    student_intrest = models.ForeignKey(intrests, on_delete=models.SET_NULL, null = True)
    student_skill = models.ManyToManyField(skills)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super(students, self).save(*args, **kwargs)

        img = Image.open(self.student_image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            #img = img.resize((300, 300))
            img.save(self.student_image.path) # Save it again and override the larger image


class occupations(models.Model):
    occupation_name = models.CharField(max_length=50)
    occupation_description = models.CharField(max_length=50)
    
    ocuupation_skill = models.ManyToManyField(skills)
    occupation_intrest = models.ForeignKey(intrests, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.occupation_name