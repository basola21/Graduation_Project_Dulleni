from django.shortcuts import render


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