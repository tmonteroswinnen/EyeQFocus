from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'pages-login.html')


class TestView(TemplateView):
    template_name = 'test.html'
