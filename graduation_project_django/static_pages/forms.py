from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student , Answer


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	
	# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_image', 'student_college', 'student_location', 'birth_date', 'student_skill']

class AnswersForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
