from django.db import models
from core.models import Patient

class ColorVisionTest(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    # Red/Green test
    rg_score = models.IntegerField(blank=True, null=True)
    rg_result = models.CharField(max_length=50, blank=True, null=True)
    rg_chart = models.ImageField(upload_to='color_vision/charts', blank=True, null=True)
    # Blue/Yellow test
    by_score = models.IntegerField(blank=True, null=True)
    by_result = models.CharField(max_length=50, blank=True, null=True)
    by_chart = models.ImageField(upload_to='color_vision/charts', blank=True, null=True)

