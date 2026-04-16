from django.conf import settings
from django.db import models


class Patient(models.Model):
	class Gender(models.TextChoices):
		MALE = 'male', 'Male'
		FEMALE = 'female', 'Female'
		OTHER = 'other', 'Other'

	name = models.CharField(max_length=200)
	age = models.PositiveIntegerField()
	gender = models.CharField(max_length=10, choices=Gender.choices)
	address = models.TextField(blank=True)
	medical_history = models.TextField(blank=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
	is_deleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return self.name
