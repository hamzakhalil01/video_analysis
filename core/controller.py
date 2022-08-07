from core.serializers import ProjectSerializer, VideoSerializer, QuestionSerializer
from core.helper import create_response, get_default_query_param
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q


class ProjectController:
    serializer_class = ProjectSerializer

    def create(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            instance = serialized_data.save()
            return create_response(self.serializer_class(instance).data, "Success", 200)
        else:
            return create_response({}, "Something went wrong", 400)

    def get_listing(self, request):
        if "id" not in request.query_params:
            limit = get_default_query_param(request, "limit", None)
            offset = get_default_query_param(request, "offset", None)
            search = get_default_query_param(request, "search", None)
            data = self.serializer_class.Meta.model.objects.all()
            if limit and offset:
                pagination = LimitOffsetPagination()
                data = pagination.paginate_queryset(data, request)
            return create_response(self.serializer_class(data, many=True).data, "Success", 200)
        data = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id"))
        if not data:
            return create_response({}, "Project not found", 400)
        return create_response(self.serializer_class(data, many=True).data, "Success", 200)

    def update_listing(self, request):
        if "id" not in request.query_params:
            return create_response({}, "user id not provided", 400)
        else:
            instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id")).first()
            if not instance:
                return create_response({}, "User not found", 404)
            serializer_data = self.serializer_class(instance, data=request.data, partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
            return create_response(serializer_data.data, "Success", 200)

    def delete_listing(self, request):
        if "id" not in request.query_params:
            return create_response({}, "user id not provided", 400)
        self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id")).delete()
        return create_response({}, "Success", 200)


class VideoController:
    serializer_class = VideoSerializer

    def create(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            instance = serializer_data.save()
            return create_response(self.serializer_class(instance).data, "Success", 200)
        return create_response({}, serializer_data.errors, 400)

    def get(self, request):
        if "id" not in request.query_params:
            limit = get_default_query_param(request, "limit", None)
            offset = get_default_query_param(request, "offset", None)
            project = get_default_query_param(request, "project_id", None)

            data = self.serializer_class.Meta.model.objects.filter1(project=project)
            if limit and offset:
                pagination = LimitOffsetPagination()
                data = pagination.paginate_queryset(data, request)
            return create_response(self.serializer_class(data, many=True).data, "Success", 200)

        else:
            instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id")).first()
            if not instance:
                return create_response({}, "Video not found", 400)
            return create_response(self.serializer_class(instance).data, "Success", 200)

    def update(self, request):
        if "id" not in request.query_params:
            return create_response({}, "Video id not provided", 400)
        else:
            instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id")).first()
            if not instance:
                return create_response({}, "Video not found", 400)
            serialized_data = self.serializer_class(instance, data=request.data, partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                return create_response(serialized_data.data, "Success", 200)
            create_response({}, "Something went wrong", 400)

    def delete(self, request):
        if "id" not in request.query_params:
            return create_response({}, "Video id not provided", 400)

        self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id")).delete()
        return create_response({}, "Success", 200)


class QuestionsController:
    serializer_class = QuestionSerializer

    def create(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            instance = serializer_data.save()
            return create_response(self.serializer_class(instance).data, "Success", 200)
        create_response({}, serializer_data.errors, 400)

    def get(self, request):
        if "id" not in request.query_params:
            return create_response(self.serializer_class(
                self.serializer_class.Meta.model.objects.all(), many=True).data,
                                   "Success", 200)
        instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id")).first()
        if not instance:
            return create_response({}, "Question not found", 400)
        return create_response(self.serializer_class(instance).data, "Success", 200)

    def update(self, request):
        if "id" not in request.query_params:
            return create_response({}, "Question id not provided", 400)
        instance = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id")).first()
        if not instance:
            return create_response({}, "Question not found", 400)
        serialized_data = self.serializer_class(instance, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return create_response(serialized_data.data, "Success", 200)
        return create_response({}, serialized_data.errors, 400)

    def delete(self, request):
        if "id" not in request.query_params:
            return create_response({}, "Question id not provided", 400)

        self.serializer_class.Meta.model.objects.filter(
            id=request.query_params.get("id")).delete()
        return create_response({}, "Success", 200)
