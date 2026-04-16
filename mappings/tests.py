from django.urls import reverse

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase

from accounts.models import User
from doctors.models import Doctor
from patients.models import Patient
from .models import PatientDoctorMapping


class MappingAPITests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(email='owner@example.com', name='Owner', password='StrongPass123')
		self.other_user = User.objects.create_user(email='outsider@example.com', name='Outsider', password='StrongPass123')
		self.patient = Patient.objects.create(
			name='John Doe',
			age=42,
			gender='male',
			address='Ward 3',
			medical_history='Diabetes',
			created_by=self.user,
		)
		self.doctor = Doctor.objects.create(
			name='Dr. House',
			specialization='Diagnostics',
			phone_number='1111111111',
			email='house@example.com',
			years_of_experience=20,
			created_by=self.user,
		)
		token = RefreshToken.for_user(self.user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

	def test_user_can_create_and_view_mappings(self):
		create_response = self.client.post(
			reverse('mapping-list-create'),
			{
				'patient_id': self.patient.id,
				'doctor_id': self.doctor.id,
			},
			format='json',
		)

		self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(PatientDoctorMapping.objects.count(), 1)

		list_response = self.client.get(reverse('mapping-detail-or-patient-doctors', args=[self.patient.id]))
		self.assertEqual(list_response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(list_response.data['doctors']), 1)

	def test_user_can_delete_mapping(self):
		mapping = PatientDoctorMapping.objects.create(
			patient=self.patient,
			doctor=self.doctor,
			created_by=self.user,
		)

		delete_response = self.client.delete(reverse('mapping-detail-or-patient-doctors', args=[mapping.id]))
		self.assertEqual(delete_response.status_code, status.HTTP_200_OK)
		self.assertEqual(PatientDoctorMapping.objects.count(), 0)
