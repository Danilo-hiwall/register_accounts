# Generated by Django 5.1.4 on 2025-01-11 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_contas_opcao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='opcao',
            field=models.CharField(choices=[('Sim', 'sim'), ('Não', 'Não')], max_length=3, verbose_name='Pago'),
        ),
    ]
