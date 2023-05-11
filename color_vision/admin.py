from django.contrib import admin
from .models import ColorVisionTest

class ColorVisionTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'rg_score', 'by_score',)
    list_filter = ('patient', 'date',)
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__email',)
    readonly_fields = ('date',)
    fieldsets = (
        (None, {
            'fields': ('patient', 'date',)
        }),
        ('Red/Green Test', {
            'fields': ('rg_score', 'rg_result', 'rg_chart',)
        }),
        ('Blue/Yellow Test', {
            'fields': ('by_score', 'by_result', 'by_chart',)
        }),
    )

admin.site.register(ColorVisionTest, ColorVisionTestAdmin)
