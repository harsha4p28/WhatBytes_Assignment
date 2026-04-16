from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
	permission_classes = [IsAuthenticated]

# Create your views here.
