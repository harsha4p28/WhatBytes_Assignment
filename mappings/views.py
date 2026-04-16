from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from doctors.serializers import DoctorSerializer
from patients.models import Patient

from .models import PatientDoctorMapping
from .serializers import MappingSerializer


class MappingListCreateView(generics.ListCreateAPIView):
	queryset = PatientDoctorMapping.objects.filter(is_deleted=False).select_related('patient', 'doctor', 'created_by')
	serializer_class = MappingSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)


class MappingDetailView(generics.DestroyAPIView):
	queryset = PatientDoctorMapping.objects.filter(is_deleted=False)
	permission_classes = [IsAuthenticated]

	def get(self, request, pk):
		patient = get_object_or_404(Patient, id=pk, created_by=request.user, is_deleted=False)
		mappings = PatientDoctorMapping.objects.filter(patient=patient, is_deleted=False).select_related('doctor')
		doctors = [DoctorSerializer(mapping.doctor).data for mapping in mappings]
		return Response(
			{
				'patient_id': patient.id,
				'patient_name': patient.name,
				'doctors': doctors,
			},
			status=status.HTTP_200_OK,
		)

	def delete(self, request, pk):
		mapping = get_object_or_404(PatientDoctorMapping, id=pk, is_deleted=False)
		mapping.is_deleted = True
		mapping.deleted_at = timezone.now()
		mapping.save(update_fields=['is_deleted', 'deleted_at'])
		return Response({'message': 'Mapping removed successfully.'}, status=status.HTTP_200_OK)

# Create your views here.
