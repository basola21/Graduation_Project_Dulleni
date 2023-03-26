from django.urls import path
from .views import home ,about, blog, contact, faqs, jobs

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('faqs', faqs, name='faqs'),
    path('jobs', jobs, name='jobs'),
]
