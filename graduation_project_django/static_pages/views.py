from django.shortcuts import render,redirect
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm ,AnswersForm
from .models import Question
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# there is a better way of doing this using class based views 
# which is more efficient and easier to read but we will stick with this for now 
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
            
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'register.html', {'register_form': form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")


def home(request):
    return render(request , "index.html")

def about(request):
    return render(request , "about.html")

def blog(request):
    return render(request , "blog.html")

def contact(request):
    return render(request , "contact.html")

def faqs(request):
    return render(request , "faqs.html")

def jobs(request):
    return render(request , "jobs.html")

def profile1(request):
    return render(request , "profile1.html")

# Update it here
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.students)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.students)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

# Intrest test section

@login_required
def intrest_test(request, page = 1):
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    try:
        question = paginator.page(page)
    except EmptyPage:
        return redirect('intrest_test', page=paginator.num_pages)
    print(f"Current page: {question.number}")


    if request.method == 'POST':
        form = AnswersForm(request.POST)
        if form.is_valid():
            form.save()
            if question.has_next():
                next_page = question.next_page_number()
                print(f"Next page: {next_page}")
                return redirect('intrest_test', page=next_page)
            else:
                return redirect('result')
    else:
        form = AnswersForm()
    print(f"Page: {page}")
    return render(request, 'intrest_test.html', {'form': form, 'question': question, 'page': page})

def result(request):
    return render(request, 'result.html')