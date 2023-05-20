import csv
from django.core.management import BaseCommand
from static_pages.models import Course, Skill


def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return 0.0


with open('/Users/basel/Documents/Projects/Grad Proj/graduation_project_django/scripts/courses.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        course = Course(
            course_name=row['Course Name'],
            university=row['University'],
            difficulty_level=row['Difficulty Level'],
            course_rating=convert_to_float(row['Course Rating']),
            course_url=row['Course URL'],
            course_description=row['Course Description'],
            extracted_skills=row['Extracted Skills']
        )
        course.save()

        # Link skills to the course
        skill_names = row['Extracted Skills'].split(',')
        for skill_name in skill_names:
            skill_name = skill_name.strip()
            if skill_name:
                skill, _ = Skill.objects.get_or_create(skill_name=skill_name)
                course.skills.add(skill)
