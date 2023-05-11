from django.db import models
import core
from core.models import Patient


class Exam(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Test(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50, choices=(('line', 'Line optotype'), ('number', 'Number optotype'), ('color', 'Color vision test')))
    result = models.FloatField()
    notation = models.CharField(max_length=10, blank=True, null=True)
    is_astigmatic = models.BooleanField(default=False)

class ETDRS(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    rows = models.PositiveSmallIntegerField()
    columns = models.PositiveSmallIntegerField()
    chart = models.TextField()

class OptokineticTest(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    speed = models.PositiveSmallIntegerField()
    direction = models.CharField(max_length=1, choices=(('H', 'Horizontal'), ('V', 'Vertical')))
