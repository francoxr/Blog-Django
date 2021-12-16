from django.shortcuts import render
from .models import Project

# Create your views here.
def briefcase(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/briefcase.html', {'projects': projects})


def detail_proyect(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'portfolio/proyect_detail.html', {'project': project})