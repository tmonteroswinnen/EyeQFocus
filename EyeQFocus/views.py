from django.shortcuts import render
from django.views.generic import TemplateView
from PIL import Image, ImageDraw, ImageFont
import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO


def home(request):
    return render(request, 'pages-login.html')


class TestView(TemplateView):
    template_name = 'index.html'


class RedGreenView(TemplateView):
    template_name = 'tests/red-green.html'


class AstigmaticView(TemplateView):
    template_name = 'tests/astigmatic.html'


class FiguresView(TemplateView):
    template_name = 'tests/figures.html'


class ColorVisionView(TemplateView):
    template_name = 'tests/color-vision.html'


from django.http import HttpResponse
from PIL import Image, ImageDraw
import random

def generar_optotipo_ninos(request):
    if request.method == 'GET':
        # Lógica para generar el optotipo y renderizarlo en un template
        # Crea una imagen en blanco
        imagen = Image.new('RGB', (200, 200), 'white')
        draw = ImageDraw.Draw(imagen)

        # Define una lista de figuras de optotipos para niños
        figuras = ['círculo', 'cuadrado', 'triángulo', 'estrella']

        # Elije una figura al azar de la lista
        figura = random.choice(figuras)

        # Dibuja la figura en la imagen
        if figura == 'círculo':
            draw.ellipse((50, 50, 150, 150), fill='black')
        elif figura == 'cuadrado':
            draw.rectangle((50, 50, 150, 150), fill='black')
        elif figura == 'triángulo':
            draw.polygon([(50, 150), (100, 50), (150, 150)], fill='black')
        elif figura == 'estrella':
            draw.polygon([(100, 25), (115, 75), (165, 75), (125, 105), (145, 155),
                          (100, 120), (55, 155), (75, 105), (35, 75), (85, 75)], fill='black')

        # Guarda la imagen en un objeto de respuesta
        response = HttpResponse(content_type="image/png")
        imagen.save(response, "PNG")
        return response

    elif request.method == 'POST':
        # Lógica para procesar los datos enviados en la solicitud POST
        # y generar el optotipo
        return HttpResponse('Optotipo generado correctamente.')



