from django.shortcuts import render
from .models import JobPost

def home(request):
    jobs = JobPost.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})