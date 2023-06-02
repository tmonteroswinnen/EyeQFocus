"""
URL configuration for EyeQFocus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

from EyeQFocus import settings
from motion_vision import views as motion_vision_views
from .views import TestView, RedGreenView, AstigmaticView, FiguresView, generar_optotipo_ninos, ColorVisionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('motion_vision/', include('motion_vision.urls')),
    path('', TestView.as_view(), name='index'),
    path('tests/red-green.html', RedGreenView.as_view(), name='red-green'),
    path('tests/astigmatic.html', AstigmaticView.as_view(), name='astigmatic'),
    path('tests/figures.html', FiguresView.as_view(), name='figures'),
    path('tests/color-vision.html', ColorVisionView.as_view(), name='color-vision'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


