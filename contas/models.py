from django.db import models

MONTH_CHOICES = (
    ('JAN', 'Janeiro'),
    ('FEB', 'Fevereiro'),
    ('MAR', 'Março'),
    ('APR', 'Abril'),
    ('MAY', 'Maio'),
    ('JUN', 'Junho'),
    ('JUL', 'Julho'),
    ('AUG', 'Agosto'),
    ('SEP', 'Setembro'),
    ('OCT', 'Outubro'),
    ('NOV', 'Novembro'),
    ('DEC', 'Dezembro'),
)


class Contas(models.Model):
    month = models.CharField(max_length=100, choices=MONTH_CHOICES)
    name_accounts = models.CharField(max_length=200)
    matury = models.DateField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    annotation = models.CharField(max_length=200)

    def __str__(self):
        return self.name_accounts
