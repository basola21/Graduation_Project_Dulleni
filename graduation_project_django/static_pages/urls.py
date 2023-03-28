from django.urls import path
from .views import home ,about, blog, contact, faqs, jobs, login_request, register_request,logout_request

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('faqs', faqs, name='faqs'),
    path('jobs', jobs, name='jobs'),
    path('login', login_request, name='login'),
    path('register', register_request, name='register'),
    path("logout", logout_request, name= "logout"),
]
