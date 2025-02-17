from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ProjectForm, MessageForm
from django.contrib import messages
from .models import Project, Message  # Import both Project and Message models


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

def index(request):
    return render(request, 'index.html')  # Will create index.html later

def project_list(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'project_list.html', {'projects': projects})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Automatically log in the user
            messages.success(request, 'Account created and logged in successfully!')
            return redirect("project_list")  # Redirect to the project list page
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def inbox(request):
    received_messages = Message.objects.filter(recipient=request.user)
    return render(request, "inbox.html", {"messages": received_messages})

def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Manually assign sender
            message.save()
            return redirect("inbox")
    else:
        form = MessageForm()
    return render(request, "send_message.html", {"form": form})
