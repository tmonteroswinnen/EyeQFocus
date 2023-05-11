from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import core.models

class Optotype(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='optotypes/')

    def __str__(self):
        return self.name


class MotionVisionTest(models.Model):
    optotypes = models.ManyToManyField(Optotype)
    optotype_order = models.CharField(max_length=20, help_text='Comma separated list of optotype IDs in order')
    rotation_speed = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text='Speed of the rotating optotypes (1-10)'
    )
    correct_direction = models.CharField(max_length=50, help_text='Direction of rotation (e.g. "clockwise")')

    def __str__(self):
        return f"Motion vision test {self.pk}"
