from django.contrib import admin
from .models import Skill, Course, Student, Occupation,Answer,Question

# Register your models here.
admin.site.register(Skill)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Occupation)
admin.site.register(Answer)
admin.site.register(Question)

admin.site.site_header = "Graduation Project Admin"
admin.site.site_title = "Graduation Project Admin Portal"
admin.site.index_title = "Welcome to Graduation Project Portal"
