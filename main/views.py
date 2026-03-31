from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ViewCount, Project, Message

def home(request):
    view_count, _ = ViewCount.objects.get_or_create(pk=1)
    view_count.count += 1
    view_count.save()

    projects = Project.objects.all()
    return render(request, 'main/home.html', {'view_count': view_count.count, 'projects': projects})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')
        
        if name and email and message_content:
            Message.objects.create(name=name, email=email, message=message_content)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    
    return render(request, 'main/contact.html')

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': all_projects})
