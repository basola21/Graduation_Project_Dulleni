from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import students , Answer


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
        model = students
        fields = ['student_image', 'student_college', 'studnet_location', 'birth_date', 'student_skill']

class AnswersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Answer
        fields = ['answer']

    def save(self, commit=True):
        answer = super().save(commit=False)
        answer.user = self.user
        answer.question = self.question
        if commit:
            answer.save()
        return answer