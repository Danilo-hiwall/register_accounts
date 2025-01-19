from rest_framework import serializers
from contas.models import Contas


class ContaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contas
        fields = '__all__'

    def validate_matury(self, value):
        if value.year < 2023:
            raise serializers.ValidationError(
                'Não é permitido inserir datas anteriores a 2023.')
        return value