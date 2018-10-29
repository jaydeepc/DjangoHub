from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='user'),
    url(r'^allprojects/$', views.projects, name='projects'),
    url(r'^api/data/$', views.get_count_by_office, name='api-data'),
    url(r'^api/office-dist-data/$', views.OfficeDistribution.as_view()),
]
