from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import RepoDetails, Contributors
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests


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


@api_view(['GET'])
def get_techstack_count(request):
    column_name = 'project_techstack'
    projects = RepoDetails.objects.values(column_name).order_by(column_name).annotate(total=Count(column_name)).exclude(project_techstack__exact='NA')
    response = projects
    return Response(response)


class OfficeDistribution(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        try:
            contributors = Contributors.objects.all().values('office').annotate(total=Count('office'))
            response = []
            for entry in contributors:
                response.append({'office': entry['office'], 'count': entry['total']})
        except:
            response = json.dumps([{'Error': 'No such office'}])
        return Response(response)