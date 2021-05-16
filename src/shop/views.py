from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from shop.models import Shop
from shop.serializers import ShopSerializer
from user.permissions import IsSuperUser


class ShopListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsSuperUser)
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user, )

class ShopRetrieveUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsSuperUser)
    queryset = Shop.objects.filter()
    serializer_class = ShopSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save()
