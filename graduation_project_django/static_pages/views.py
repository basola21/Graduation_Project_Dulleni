from django.shortcuts import render,redirect
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm ,AnswersForm
from .models import Question, Answer,Occupation
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



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
    jobs = Occupation.objects.all()
    paginator = Paginator(jobs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request , "jobs.html",{'page_obj': page_obj})

def profile1(request):
    return render(request , "profile1.html")

# Update it here
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.student)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.student)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

# Intrest test section

@login_required
def intrest_test(request, page = 1):
    questions = Question.objects.all()
    form = AnswersForm()


    paginator = Paginator(questions, 1)
    page = paginator.get_page(page)

    question = Question.objects.get(pk=page.object_list[0].id)

    context = {'question':question.question,'form':form}

    if request.method == 'POST':
        form = AnswersForm(request.POST)
        if form.is_valid():

            # Get the current user
            user = request.user
            student = user.student

            # Get the Question object corresponding to the selected question ID
            question = Question.objects.get(pk=page.object_list[0].id)

            try:
                answer = Answer.objects.get(user=student, question=question)
                # Update the existing answer
                answer.answer = form.cleaned_data['answer']
                answer.save()
                messages.success(request, 'Your answer has been updated!')
                
            except Answer.DoesNotExist:
                # Create a new answer instance for this user and question
                answer = form.save(commit=False)
                answer.user = student
                answer.question = question
                answer.save()
                messages.success(request, 'Your answer has been saved!')
            
            if page.has_next():
                next_page = str(page.next_page_number())
                return redirect('intrest_test', page=next_page)
            else:
                return redirect('result')
        else:
            messages.error(request, 'Please select an answer for all questions')
    else:
        # return a response when request is not a POST request
        return render(request, 'intrest_test.html', context)
    
    return render(request, 'intrest_test.html', context)

@login_required
def result(request):

    interest_types = ["realistic", "investigative", "artistic", "social", "enterprising", "conventional"]
    scoredict = {}

    # Retrieve user's answers from Answers table
    user_id = request.user.id
    user_answers = Answer.objects.filter(user=user_id)

    # Calculate scores for each interest type
    for interest_type in interest_types:
        questions = Question.objects.filter(question_type=interest_type)
        if not questions:
            print(f"No questions found for interest type: {interest_type}")
            continue

        score = 0
        for question in questions:
            answer = user_answers.filter(question=question).first()
            if not answer:
                print(f"No answer found for question: {question.question}")
                continue

            score += answer.answer

        scoredict[interest_type] = score
        print(f"Score for interest type {interest_type}: {score}")

    # Determine interest type with highest score
    max_score = max(scoredict.values())
    interest_type = [key for key, value in scoredict.items() if value == max_score][0]

    student = request.user.student
    student.student_interest = interest_type
    student.save()

    return render(request, 'result.html', {'interest_type': interest_type})

@login_required
def career(request):
    student = request.user.Student
    interest_type = student.student_intrest
    occupations = Occupation.objects.filter(occupation_type=interest_type)
    return render(request, 'career.html', {'occupations': occupations})

@login_required
def skill_match(request):
    student = request.user.student
    student_skills = student.student_skill.all()
    
    # Calculate the matching percentage for each occupation
    occupation_matches = []
    for occupation in Occupation.objects.all():
        matching_skills = set(occupation.occupation_skill.all()) & set(student_skills)
        match_percent = round(len(matching_skills) / len(occupation.occupation_skill.all()) * 100)

        if match_percent > 0:
            occupation_matches.append((occupation, match_percent))

    # Sort the occupations by matching percentage in descending order
    occupation_matches.sort(key=lambda x: x[1], reverse=True)

    return render(request, 'skill_match.html', {'occupation_matches': occupation_matches})

@login_required
def interst_match(request):

    student = request.user.student

    try :
       student_interest = student.student_interest
    except student.student_interest.DoesNotExist:
        messages.error(request, 'Please take the interest test first')
        return redirect('intrest_test')
    else :
        student_interest = student.student_interest.capitalize()
        print(student_interest)
        print('Investigative')

        occupation_matches = Occupation.objects.filter(occupation_interest=student_interest) 
        print(occupation_matches)

        return render(request, 'interest_match.html', {'occupations': occupation_matches})
        
