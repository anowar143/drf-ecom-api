from django.urls import path

from wallet.views import WalletListCreateView

app_name = 'wallet'

urlpatterns = [
    path('', WalletListCreateView.as_view(), name='wallet-create-list-api'),
]
