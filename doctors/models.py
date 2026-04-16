from django.conf import settings
from django.db import models


class Doctor(models.Model):
	name = models.CharField(max_length=200)
	specialization = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	years_of_experience = models.PositiveIntegerField(default=0)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctors')
	is_deleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return f'{self.name} - {self.specialization}'
