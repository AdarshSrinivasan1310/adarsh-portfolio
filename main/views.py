from django.shortcuts import render
from .models import ViewCount, Project

def home(request):
    view_count, _ = ViewCount.objects.get_or_create(pk=1)
    view_count.count += 1
    view_count.save()

    projects = Project.objects.all()
    return render(request, 'main/home.html', {'view_count': view_count.count, 'projects': projects})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': all_projects})
