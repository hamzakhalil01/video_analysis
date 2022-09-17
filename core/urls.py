from django.urls import path
from core.views import ProjectAPIView, VideoAPIView, QuestionsAPIView, UserVideoAPI

urlpatterns = [
    path('manage-project', ProjectAPIView.as_view(
        {
            'get': 'get_project',
            'post': 'create_project',
            'patch': 'update_project',
            'delete': 'delete_project'
        }
    )
         ),

    path('manage-video', VideoAPIView.as_view(
        {
            'get': 'get_video',
            'post': 'create_video',
            'patch': 'update_video',
            'delete': 'delete_video'
        }
    )
             ),

    path('manage-questions', QuestionsAPIView.as_view(
        {
            'get': 'get_question',
            'post': 'create_question',
            'patch': 'update_question',
            'delete': 'delete_question'
        }
    )
        ),

    path('user-video', UserVideoAPI.as_view(
            {
                'get': 'get_user_video',
                'post': 'create_user_video',
                'patch': 'update_user_video',
                'delete': 'delete_user_video'
            }
        )
            )
]
