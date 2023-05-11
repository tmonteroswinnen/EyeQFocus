from django.urls import path
from .views import MotionVisionTestView

urlpatterns = [
    path('test/', MotionVisionTestView.as_view(), name='test'),
]