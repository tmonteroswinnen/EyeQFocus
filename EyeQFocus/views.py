from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'pages-login.html')


class TestView(TemplateView):
    template_name = 'index.html'


class RedGreenView(TemplateView):
    template_name = 'tests/red-green.html'


class AstigmaticView(TemplateView):
    template_name = 'tests/astigmatic.html'