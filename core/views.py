from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.controller import ProjectController, VideoController, QuestionsController, UserVideoController

# Create your views here.
project_controller = ProjectController()
video_controller = VideoController()
quest_controller = QuestionsController()
user_controller = UserVideoController()

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


class QuestionsAPIView(ModelViewSet):

    def create_question(self, request):
        return quest_controller.create(request)

    def get_question(self, request):
        return quest_controller.get(request)

    def update_question(self, request):
        return quest_controller.update(request)

    def delete_question(self, request):
        return quest_controller.delete(request)


class UserVideoAPI(ModelViewSet):
    def create_user_video(self, request):
        return user_controller.create(request)

    def get_user_video(self, request):
        return user_controller.get(request)

    def update_user_video(self, request):
        return user_controller.update(request)

    def delete_user_video(self, request):
        return user_controller.delete(request)

