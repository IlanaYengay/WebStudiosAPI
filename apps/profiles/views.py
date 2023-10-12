from django.shortcuts import render
from .models import Profile
from rest_framework import viewsets
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

