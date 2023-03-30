from django.contrib import admin
from .models import skills, courses, intrests, students, occupations

# Register your models here.
admin.site.register(skills)
admin.site.register(courses)
admin.site.register(intrests)
admin.site.register(students)
admin.site.register(occupations)
