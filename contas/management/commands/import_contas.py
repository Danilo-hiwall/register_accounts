import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from contas.models import Contas


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com Contas',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                month = row['month']
                name_accounts = row['name_accounts']
                matury = datetime.strptime(row['matury'], '%Y-%m-%d').date()
                value = row['value']
                annotation = row['annotation']
                opcao = row['opcao']

                self.stdout.write(self.style.NOTICE(name_accounts))

                Contas.objects.create(
                    month=month,
                    name_accounts=name_accounts,
                    matury=matury,
                    value=value,
                    annotation=annotation,
                    opcao=opcao,
                )

        self.stdout.write(self.style.SUCCESS('CONTAS IMPORTADAS COM SUCESSO!'))