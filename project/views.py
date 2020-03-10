from django.shortcuts import render
from .models import Project
from .forms import ProjectFilter

# Create your views here.
def all_projects(request):
    projects = Project.objects.all()
    myFilter = ProjectFilter(request.GET, queryset=projects)
    projects = myFilter.qs
    return render(request, 'project/all_projects.html', {'projects':projects, 'myFilter':myFilter})
