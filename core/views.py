from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.controller import ProjectController, VideoController

# Create your views here.
project_controller = ProjectController()
video_controller = VideoController()

class ProjectAPIView(ModelViewSet):

    def create_project(self, request):
        return project_controller.create(request)

    def get_project(self, request):
        return project_controller.get_listing(request)

    def update_project(self, request):
        return project_controller.update_listing(request)

    def delete_project(self, request):
        return project_controller.delete_listing(request)


class VideoAPIView(ModelViewSet):

    def create_video(self, request):
        return video_controller.create(request)

    def get_video(self, request):
        return video_controller.get(request)

    def update_video(self, request):
        return video_controller.update(request)

    def delete_video(self, request):
        return video_controller.delete(request)