from rest_framework import serializers
from .models import Order, Image



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'file')


class OrderSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs={
            'order_number': {'read_only': True},
            'user': {'read_only': True},
            'status': {'read_only': True},
        }

    def create(self, validated_data):
        images = self.context['request'].FILES
        order = Order.objects.create(**validated_data)

        for images in images.values():
            Image.objects.create(order=order, file=images)

        return order

