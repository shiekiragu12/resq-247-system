from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import *
from facilities.serializers import DoctorSerializer, PatientSerializer, StaffSerializer


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(WritableNestedModelSerializer):
    profile = ProfileSerializer(required=False)
    doctor = DoctorSerializer(required=False)
    patient = PatientSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'profile', 'doctor', 'patient',
                  'staff', 'date_joined', 'last_login']

    def to_representation(self, instance):
        self.fields['doctor'] = DoctorSerializer(many=False)
        self.fields['patient'] = PatientSerializer(many=False)
        self.fields['profile'] = ProfileSerializer(many=False)
        self.fields['staff'] = StaffSerializer(many=False)
        return super(UserSerializer, self).to_representation(instance)
