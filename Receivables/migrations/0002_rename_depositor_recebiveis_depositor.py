# Generated by Django 5.1.4 on 2025-01-23 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Receivables', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recebiveis',
            old_name='Depositor',
            new_name='depositor',
        ),
    ]
