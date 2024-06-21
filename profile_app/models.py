from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    skills = models.TextField(blank=True, null=True)
    contact_details = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    project = models.TextField(blank=True, null=True)
    work_experience = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    certification = models.CharField(max_length=255)


    def __str__(self):
        return self.title