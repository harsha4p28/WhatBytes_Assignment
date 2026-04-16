from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import EmailTokenObtainPairSerializer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
	serializer_class = RegisterSerializer
	permission_classes = [AllowAny]

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		headers = self.get_success_headers(serializer.data)
		return Response(
			{
				'message': 'User registered successfully.',
				'user': {
					'id': user.id,
					'name': user.name,
					'email': user.email,
				},
			},
			status=status.HTTP_201_CREATED,
			headers=headers,
		)


class LoginView(TokenObtainPairView):
	serializer_class = EmailTokenObtainPairSerializer

# Create your views here.
