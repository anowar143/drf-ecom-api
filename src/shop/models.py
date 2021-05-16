from django.db import models
from base.models import BaseModel


class Shop(BaseModel):
    name = models.CharField(max_length=150)
    address = models.TextField(null=False)
    logo = models.URLField(null=True)
    rating = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey('user.User', on_delete=models.PROTECT)
    location = models.TextField(blank=False, default='https://maps.google.com/')



    class Meta:
        db_table = 'shops'
        verbose_name = 'Shop'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name
