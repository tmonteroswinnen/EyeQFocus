from django.contrib import admin
from .models import Optotype, MotionVisionTest


@admin.register(Optotype)
class OptotypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


@admin.register(MotionVisionTest)
class MotionVisionTestAdmin(admin.ModelAdmin):
    list_display = ['pk', 'rotation_speed', 'correct_direction']
    search_fields = ['pk', 'rotation_speed', 'correct_direction']

    def save_model(self, request, obj, form, change):
        optotype_ids = [int(optotype_id.strip()) for optotype_id in obj.optotype_order.split(',')]
        optotypes = Optotype.objects.filter(pk__in=optotype_ids)
        obj.optotypes.set(optotypes)
        super().save_model(request, obj, form, change)

