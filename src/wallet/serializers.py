from rest_framework import serializers
from wallet.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Wallet
        fields = '__all__'

