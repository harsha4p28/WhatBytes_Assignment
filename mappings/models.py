from django.conf import settings
from django.db import models
from django.db.models import Q

from doctors.models import Doctor
from patients.models import Patient


class PatientDoctorMapping(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_mappings')
	is_deleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		constraints = [
			models.UniqueConstraint(
				fields=('patient', 'doctor'),
				condition=Q(is_deleted=False),
				name='unique_active_patient_doctor_mapping',
			),
		]
		ordering = ('-created_at',)

	def __str__(self):
		return f'{self.patient_id} -> {self.doctor_id}'
