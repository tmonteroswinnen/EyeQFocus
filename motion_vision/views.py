from django.views.generic import TemplateView
from .models import MotionVisionTest


class MotionVisionTestView(TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = MotionVisionTest.objects.first()  # Aquí seleccionamos un objeto MotionVisionTest de la base de datos
        return context
