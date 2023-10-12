from rest_framework import serializers
from .models import CustomUser
from datetime import datetime
from apps.profiles.models import Profile


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    birthdate = serializers.DateField(write_only=True)
    first_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'birthdate', 'phone_number', 'password', 'first_name')

    def create(self, validated_data):
        birthdate = validated_data.pop('birthdate')
        first_name = validated_data.pop('first_name')
        age = datetime.now().year - birthdate.year
        if age < 18:
            raise serializers.ValidationError('Чтобы зарегистрироваться вам должно быть 18 лет')
        user = super().create(validated_data)
        Profile.objects.create(user=user, birthdate=birthdate, first_name=first_name)
        return user
