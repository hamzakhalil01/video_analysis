from core.models import Project, Video, Questions, UserVideo
from rest_framework.serializers import ModelSerializer


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class VideoSerializer(ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Questions
        fields = "__all__"



class UserVideoSerializer(ModelSerializer):

    class Meta:
        model = UserVideo
        fields = "__all__"






