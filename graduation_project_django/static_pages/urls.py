from django.urls import path
from .views import home ,about, blog, contact, faqs, jobs, login_request, register_request,logout_request,profile,register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('faqs', faqs, name='faqs'),
    path('jobs', jobs, name='jobs'),
    path('login', login_request, name='login'),
    path('register', register, name='register'),
    path("logout", logout_request, name= "logout"),
    path("profile", profile, name= "profile"),

]

# Only add this when we are in debug mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)