# Generated by Django 5.1.4 on 2025-01-08 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='month',
            field=models.CharField(choices=[('JAN', 'Janeiro'), ('FEB', 'Fevereiro'), ('MAR', 'Março'), ('APR', 'Abril'), ('MAY', 'Maio'), ('JUN', 'Junho'), ('JUL', 'Julho'), ('AUG', 'Agosto'), ('SEP', 'Setembro'), ('OCT', 'Outubro'), ('NOV', 'Novembro'), ('DEC', 'Dezembro')], max_length=100),
        ),
    ]
