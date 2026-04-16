from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import Patient
from .serializers import PatientSerializer


class PatientListCreateView(generics.ListCreateAPIView):
	serializer_class = PatientSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Patient.objects.filter(created_by=self.request.user, is_deleted=False)

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PatientSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Patient.objects.filter(created_by=self.request.user, is_deleted=False)

	def perform_destroy(self, instance):
		instance.is_deleted = True
		instance.deleted_at = timezone.now()
		instance.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])

# Create your views here.
