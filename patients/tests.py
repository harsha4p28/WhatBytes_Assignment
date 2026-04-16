from django.urls import reverse

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase

from accounts.models import User
from .models import Patient


class PatientAPITests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(email='doctor@example.com', name='Doctor One', password='StrongPass123')
		self.other_user = User.objects.create_user(email='other@example.com', name='Other User', password='StrongPass123')
		self.patient = Patient.objects.create(
			name='John Doe',
			age=42,
			gender='male',
			address='Ward 3',
			medical_history='Diabetes',
			created_by=self.user,
		)
		token = RefreshToken.for_user(self.user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

	def test_authenticated_user_can_create_and_list_own_patients(self):
		create_response = self.client.post(
			reverse('patient-list-create'),
			{
				'name': 'Jane Doe',
				'age': 29,
				'gender': 'female',
				'address': 'Ward 2',
				'medical_history': 'Asthma',
			},
			format='json',
		)

		self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(create_response.data['name'], 'Jane Doe')

		list_response = self.client.get(reverse('patient-list-create'))
		self.assertEqual(list_response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(list_response.data), 2)

	def test_patient_detail_is_scoped_to_owner(self):
		self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {RefreshToken.for_user(self.other_user).access_token}')
		detail_response = self.client.get(reverse('patient-detail', args=[self.patient.id]))
		self.assertEqual(detail_response.status_code, status.HTTP_404_NOT_FOUND)
