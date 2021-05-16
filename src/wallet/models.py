from django.db import models
from base.models import BaseModel


class Wallet(BaseModel):
    amount = models.FloatField()
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)

    class Meta:
        db_table = 'wallets'

    def __str__(self):
        return self.user.username
