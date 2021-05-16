from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from wallet.serializers import WalletSerializer
from wallet.models import Wallet


class WalletListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer
    queryset = Wallet.objects.filter()

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset
