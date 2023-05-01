from django.contrib import admin
from .models import skills, courses, intrests, students, occupations,intrestTest,Question

# Register your models here.
admin.site.register(skills)
admin.site.register(courses)
admin.site.register(intrests)
admin.site.register(students)
admin.site.register(occupations)
admin.site.register(intrestTest)
admin.site.register(Question)

admin.site.site_header = "Graduation Project Admin"
admin.site.site_title = "Graduation Project Admin Portal"
admin.site.index_title = "Welcome to Graduation Project Portal"
