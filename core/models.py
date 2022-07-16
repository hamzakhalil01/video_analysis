from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    videos = models.IntegerField(null=True, blank=True)
    respondents = models.IntegerField(null=True, blank=True)


class Video(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    video = models.FileField(max_length=250, null=True, blank=True, upload_to='videos')
    created_at = models.DateTimeField(auto_now_add=True)
    video_size = models.CharField(max_length=10, null=True, blank=True)
    sent_to_subjects = models.IntegerField(null=True, blank=True)
    respondents = models.IntegerField(null=True, blank=True)
    downloads = models.IntegerField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)


class Questions(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    question = models.CharField(max_length=250, null=True, blank=True)