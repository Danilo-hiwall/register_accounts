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

OPCOES_SIM_NAO = [
    ('Sim', 'sim'),
    ('Não', 'Não'),
]


class Contas(models.Model):
    month = models.CharField(max_length=100, choices=MONTH_CHOICES)
    name_accounts = models.CharField(max_length=200)
    matury = models.DateField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    annotation = models.CharField(max_length=200)
    pay = models.CharField(max_length=3, choices=OPCOES_SIM_NAO, verbose_name="Pago")

    def __str__(self):
        return dict(self.opcao).get(self.opcao, "Indefinido")

    def __str__(self):
        return self.name_accounts
