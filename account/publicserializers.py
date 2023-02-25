from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import *


class ProfileSerializer(serializers.ModelSerializer):

    profile_photo = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['profile_photo']

    def get_profile_photo(self, obj):
        return obj.profile_photo.url


class PubUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile', 'date_joined', 'last_login']

    def to_representation(self, instance):
        self.fields['profile'] = ProfileSerializer(many=False)
        return super(PubUserSerializer, self).to_representation(instance)
