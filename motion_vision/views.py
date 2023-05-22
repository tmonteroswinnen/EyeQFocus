from django.views.generic import TemplateView
from django.shortcuts import render
from .models import MotionVisionTest, Optotype
import json
from django.http import JsonResponse


class MotionVisionTestView(TemplateView):
    template_name = "motion_vision_test.html"

    def motion_vision_test_view(request, test_id):
        # Obtén el objeto MotionVisionTest
        motion_vision_test = MotionVisionTest.objects.get(pk=test_id)

        # Obtén los optotipos en el orden especificado por optotype_order
        optotype_order = motion_vision_test.optotype_order.split(',')
        optotypes = Optotype.objects.filter(optotype_id__in=optotype_order)

        # Convierte los optotipos a una lista serializable en JSON
        optotypes_json = json.dumps(
            [{'id': optotype.optotype_id, 'char': optotype.optotype_char} for optotype in optotypes])

        # Renderiza el archivo HTML con los datos necesarios
        return render(request, 'motion_vision_test.html', {
            'optotypes_json': optotypes_json,
            'optotype_order': motion_vision_test.optotype_order,
            'rotation_speed': motion_vision_test.rotation_speed,
            'correct_direction': motion_vision_test.correct_direction
        })

    def get_motion_vision_data(request):
        # Obtén el ID del test de visión en movimiento desde la URL
        test_id = request.GET.get('test_id')

        try:
            # Obtén el objeto MotionVisionTest
            motion_vision_test = MotionVisionTest.objects.get(pk=test_id)

            # Obtén los optotipos en el orden especificado por optotype_order
            optotype_order = motion_vision_test.optotype_order.split(',')
            optotypes = Optotype.objects.filter(optotype_id__in=optotype_order)

            # Convierte los optotipos a una lista serializable en JSON
            optotypes_json = json.dumps(
                [{'id': optotype.optotype_id, 'char': optotype.optotype_char} for optotype in optotypes])

            # Construye un diccionario con los datos
            data = {
                'optotypes_json': optotypes_json,
                'optotype_order': motion_vision_test.optotype_order,
                'rotation_speed': motion_vision_test.rotation_speed,
                'correct_direction': motion_vision_test.correct_direction
            }

            return JsonResponse(data)
        except MotionVisionTest.DoesNotExist:
            # Manejo de error si el test de visión en movimiento no existe
            return JsonResponse({'error': 'Test not found'}, status=404)