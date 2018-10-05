from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='user'),
    url(r'^allprojects/$', views.projects, name='projects'),
]
