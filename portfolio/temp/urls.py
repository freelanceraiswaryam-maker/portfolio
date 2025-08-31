from django.urls import path
from temp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
]
