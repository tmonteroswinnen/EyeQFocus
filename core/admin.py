from django.contrib import admin
from .models import Patient, VisionTest, MedicalReport

class MedicalReportInline(admin.TabularInline):
    model = MedicalReport

class VisionTestAdmin(admin.ModelAdmin):
    inlines = [MedicalReportInline]

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthdate', 'gender', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('test', 'result_text')

admin.site.register(Patient, PatientAdmin)
admin.site.register(VisionTest, VisionTestAdmin)
admin.site.register(MedicalReport, MedicalReportAdmin)
