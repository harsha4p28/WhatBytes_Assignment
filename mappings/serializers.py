from rest_framework import serializers

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from patients.models import Patient
from patients.serializers import PatientSerializer

from .models import PatientDoctorMapping


class MappingSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(write_only=True)
    doctor_id = serializers.IntegerField(write_only=True)
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient_id', 'doctor_id', 'patient', 'doctor', 'created_at')
        read_only_fields = ('id', 'patient', 'doctor', 'created_at')

    def validate(self, attrs):
        request = self.context['request']
        patient_id = attrs['patient_id']
        doctor_id = attrs['doctor_id']

        try:
            patient = Patient.objects.get(id=patient_id, created_by=request.user)
        except Patient.DoesNotExist as exc:
            raise serializers.ValidationError({'patient_id': 'Patient not found or you do not have access to it.'}) from exc

        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist as exc:
            raise serializers.ValidationError({'doctor_id': 'Doctor not found.'}) from exc

        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError('This doctor is already assigned to the patient.')

        attrs['patient'] = patient
        attrs['doctor'] = doctor
        return attrs

    def create(self, validated_data):
        validated_data.pop('patient_id', None)
        validated_data.pop('doctor_id', None)
        return PatientDoctorMapping.objects.create(**validated_data)
