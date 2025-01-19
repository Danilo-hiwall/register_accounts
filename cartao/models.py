from django.db import models
from owner.models import Dono


class Cartao(models.Model):
    owner = models.ManyToManyField(Dono, related_name='owner')
    type_card = models.CharField(max_length=100)
    closing = models.IntegerField(blank=True, null=True)
    matury = models.IntegerField(blank=True, null=True)
    limit_card = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.type_card