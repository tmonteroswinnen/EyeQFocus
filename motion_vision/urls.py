from django.urls import path
from .views import MotionVisionTestView

urlpatterns = [
    path('test/', MotionVisionTestView.as_view(), name='test'),
    path('motion_vision_test/<int:test_id>/', MotionVisionTestView.as_view(), name='motion_vision_test'),
    path('get_motion_vision_data/', MotionVisionTestView.as_view(), name='get_motion_vision_data')
]
