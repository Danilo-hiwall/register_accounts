from rest_framework import serializers
from contas.models import Contas
from django.db import models


class ContaModelSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Contas
        fields = ['id', 'month', 'name_accounts', 'matury', 'value', 'annotation', 'opcao', 'total']


    def get_total(self, obj):
        return Contas.objects.aggregate(total_sum=models.Sum('value'))['total_sum'] or 0

    def validate_matury(self, value):
        if value.year < 2023:
            raise serializers.ValidationError(
                'Não é permitido inserir datas anteriores a 2023.')
        return value