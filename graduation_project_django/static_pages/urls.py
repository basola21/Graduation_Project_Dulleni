from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/<int:job_id>/', views.job_details, name='job_details'),
    path('login', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path("logout", views.logout_request, name= "logout"),
    path("profile/", views.profile, name= "profile"),
    path("intrest-test/", views.intrest_test, name = "intrest_test"),
    path("intrest-test/<page>/", views.intrest_test, name = "intrest_test"),
    path("result/", views.result, name = "result"),
    path("jobs/skill-match/", views.skill_match, name = "skill_match"),
    path("jobs/interst-match/", views.interst_match, name = "interst_match"),

    
]

# Only add this when we are in debug mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)