from django.contrib import admin
from .models import Exam, Test, ETDRS, OptokineticTest

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'date')
    list_filter = ('patient', 'date')
    search_fields = ('patient__name',)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam', 'test_type', 'result', 'is_astigmatic')
    list_filter = ('exam__patient', 'test_type', 'is_astigmatic')
    search_fields = ('exam__patient__name',)

@admin.register(ETDRS)
class ETDRSAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam', 'rows', 'columns')
    list_filter = ('exam__patient', 'rows', 'columns')
    search_fields = ('exam__patient__name',)

@admin.register(OptokineticTest)
class OptokineticTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam', 'speed', 'direction')
    list_filter = ('exam__patient', 'speed', 'direction')
    search_fields = ('exam__patient__name',)
