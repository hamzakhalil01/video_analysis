from django.urls import path
from core.views import ProjectAPIView, VideoAPIView

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
             )
]
