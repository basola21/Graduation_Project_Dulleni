import os


from static_pages.models import Question

# Define a dictionary to map file names to question types
type_mapping = {
    'realistic.txt': 'realistic',
    'investigative.txt': 'investigative',
    'artistic.txt': 'artistic',
    'social.txt': 'social',
    'enterprising.txt': 'enterprising',
    'conventional.txt': 'conventional',
}

# Define the path to the directory containing the text files
text_file_dir = '/Users/basel/Documents/Projects/Grad Proj/graduation_project_django/scripts/Questions'

# Loop through each file in the directory
for filename in os.listdir(text_file_dir):
    # Get the question type for the file
    question_type = type_mapping.get(filename)
    if question_type is None:
        continue
    
    # Open the file and read each line
    with open(os.path.join(text_file_dir, filename), 'r') as f:
        lines = f.readlines()
    
    # Create a Question object for each line and save it to the database
    for line in lines:
        question = line.strip()
        q = Question(question=question, questionType=question_type)
        q.save()
