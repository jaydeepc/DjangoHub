from django.db import models
from django.db import models


class RepoDetails(models.Model):

    user_firstname = models.CharField(max_length=25)
    user_lastname = models.CharField(max_length=25)
    project_name = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    office = models.CharField(max_length=25)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_techstack = models.CharField(max_length=25)
    user_photo = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.project_name

