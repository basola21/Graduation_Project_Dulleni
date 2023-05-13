import csv
from static_pages.models import Occupation, Skill

with open('/Users/basel/Documents/Projects/Grad Proj/graduation_project_django/scripts/occupation.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        occupation = Occupation.objects.create(
            occupation_name=row['title'],
            occupation_description=row['descriptionskills'],
            occupation_interest=row['intrest']
        )
        
        # create skills objects
        skills_list = row['skills'].split(',')
        for skill_name in skills_list:
            skill, _ = Skill.objects.get_or_create(skill_name=skill_name.strip())
            occupation.occupation_skill.add(skill)

        occupation.save()
