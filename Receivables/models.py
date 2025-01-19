from django.db import models
from owner.models import Dono


PAYMENT_CHOICES = (
    ('PIX', 'Pix'),
    ('DINHEIRO', 'Dinheiro'),
    ('CARTÂO', 'Cartão'),
    ('CHEQUE', 'Cheque'),
    
)


class recebiveis(models.Model):
    entry_date = models.DateField(null=True,blank=True)
    entries_of = models.ManyToManyField(Dono, related_name='entries_of')
    value = models.IntegerField(null=True, blank=True)
    Depositor = models.CharField(max_length=200, blank=True, null=True)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_CHOICES, null=True, blank=True)
    resume = models.TextField(max_length=500, null=True, blank=True)