from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import core.models


class Optotype(models.Model):
    optotype_id = models.CharField(max_length=50, unique=True)
    optotype_char = models.CharField(max_length=5)
    optotype_image = models.ImageField(upload_to='optotypes/', null=True, blank=True)

    def __str__(self):
        return self.optotype_id

    class Meta:
        ordering = ['optotype_id']


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
