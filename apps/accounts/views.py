from .models import CustomUser
from .serializers import CustomUserSerializer
from .filters import CustomUserFilter
from rest_framework import viewsets

class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


