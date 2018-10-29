from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import RepoDetails, Contributors
import json
from rest_framework.views import APIView
from rest_framework.response import Response


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


def get_count_by_office(request):
    if request.method == "GET":
        try:
            contributors = Contributors.objects.all().values('office').annotate(total=Count('office'))
            response = []
            for entry in contributors:
                response.append({'office': entry['office'], 'count': entry['total']})
        except:
            response = json.dumps([{'Error': 'No such office'}])

    return JsonResponse(response, safe=False)


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