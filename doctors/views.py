from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
	queryset = Doctor.objects.filter(is_deleted=False)
	serializer_class = DoctorSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Doctor.objects.filter(is_deleted=False)
	serializer_class = DoctorSerializer
	permission_classes = [IsAuthenticated]

	def perform_destroy(self, instance):
		instance.is_deleted = True
		instance.deleted_at = timezone.now()
		instance.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])

# Create your views here.
