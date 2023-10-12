from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'birthdate', 'first_name', 'last_name', 'bio', 'age', 'photo']
        extra_kwargs = {
            'age': {'read_only': True}
        }
