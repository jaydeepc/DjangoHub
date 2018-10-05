import requests
from django.http import HttpResponse
from django.shortcuts import render
from .models import RepoDetails


def index(request):

    projects = RepoDetails.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)


def projects(request):

    projects = RepoDetails.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)
