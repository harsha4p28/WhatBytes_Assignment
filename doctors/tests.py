from django.urls import reverse

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase

from accounts.models import User


class DoctorAPITests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(email='doctor@example.com', name='Doctor One', password='StrongPass123')
		token = RefreshToken.for_user(self.user)
		self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')

	def test_authenticated_user_can_create_and_list_doctors(self):
		create_response = self.client.post(
			reverse('doctor-list-create'),
			{
				'name': 'Dr. Strange',
				'specialization': 'Cardiology',
				'phone_number': '1234567890',
				'email': 'strange@example.com',
				'years_of_experience': 12,
			},
			format='json',
		)

		self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
		list_response = self.client.get(reverse('doctor-list-create'))
		self.assertEqual(list_response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(list_response.data), 1)
