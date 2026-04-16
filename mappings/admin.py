from django.contrib import admin

from .models import PatientDoctorMapping


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
	list_display = ('patient', 'doctor', 'created_by', 'created_at')
	search_fields = ('patient__name', 'doctor__name', 'created_by__email')
