from django.contrib import admin

from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display = ('name', 'specialization', 'years_of_experience', 'created_by', 'created_at')
	search_fields = ('name', 'specialization', 'email')
	list_filter = ('specialization', 'created_at')
