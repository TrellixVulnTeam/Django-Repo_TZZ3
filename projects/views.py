from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context )


def project(request,pk):
    projectobj = Project.objects.get(id=pk)
   
    return render(request, 'projects/single-project.html',{'project':projectobj })


def createProject(request):
    context = {}
    return render(request, "projects/project_form.html", context)
