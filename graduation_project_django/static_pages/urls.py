from django.urls import path
from .views import home ,about, blog, contact, faqs, jobs, login_request, result,logout_request,profile,register,intrest_test, jobs,skill_match,interst_match
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('faqs/', faqs, name='faqs'),
    path('jobs/', jobs, name='jobs'),
    path('login', login_request, name='login'),
    path('register/', register, name='register'),
    path("logout", logout_request, name= "logout"),
    path("profile/", profile, name= "profile"),
    path("intrest-test/",intrest_test, name = "intrest_test"),
    path("intrest-test/<page>/",intrest_test, name = "intrest_test"),
    path("result/",result, name = "result"),
    path("jobs/skill-match/",skill_match, name = "skill_match"),
    path("jobs/interst-match/",interst_match, name = "interst_match"),

    
]

# Only add this when we are in debug mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)