from rest_framework import serializers
from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    owner_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'
