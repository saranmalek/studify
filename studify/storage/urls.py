# myapp/urls.py
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line to include the admin interface
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('afterhome/', views.afterhomePage, name='afterhome'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),
    path('essay/', views.eassyPage, name='essay'),
    path('homework/', views.homeworkPage, name='homework'),
    path('gk/', views.GKPage, name='gk'),
    path('punctuation/', views.punctuationPage, name='punctuation'),
    path('quiz/', views.quizPage, name='quiz'),
    path('generate-essay/', views.generate_essay, name='generate_essay'),
    path("your-api-url-to-get-gk-response", views.get_gk_response, name="get_gk_response"),
    path('get_homework_solution/', views.get_homework_solution, name='get_homework_solution'),
    path('generate_quiz/', views.generate_quiz, name='generate_quiz'),
     path('correct-punctuation/', views.correct_punctuation, name='correct_punctuation'),
]