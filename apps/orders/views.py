from .models import Order, Image
from .serializers import OrderSerializer, ImageSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_authenticated:
            queryset = queryset.filter(user=None)
        return queryset



class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer