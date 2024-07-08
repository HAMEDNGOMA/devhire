from django.shortcuts import render
from .models import Project
# Create your views here.




def projects(request):
    dev_projects = Project.objects.all()
    context = {'projects': dev_projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    context = {'project': project_obj}

    return render(request, "projects/single-project.html", context)
def  createProject(request):

    return  render(request,'projects/project_form.html')