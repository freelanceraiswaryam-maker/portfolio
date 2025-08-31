from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'temp/home.html')
def contact(request):
    return render(request,'temp/contact.html')
def projects(request):
    return render(request,'temp/projects.html')
def resume(request):
    return render(request,'temp/resume.html')