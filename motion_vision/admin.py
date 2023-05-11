from django.contrib import admin
from .models import Optotype, MotionVisionTest

@admin.register(Optotype)
class OptotypeAdmin(admin.ModelAdmin):
    list_display = ('optotype_id', 'optotype_char', 'optotype_image')
    search_fields = ('optotype_id', 'optotype_char')

@admin.register(MotionVisionTest)
class MotionVisionTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'rotation_speed', 'correct_direction')
    filter_horizontal = ('optotypes',)
