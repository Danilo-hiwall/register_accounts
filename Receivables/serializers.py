from rest_framework import serializers
from Receivables.models import recebiveis


class ReceivablesSerializer(serializers.ModelSerializer):

    class Meta:
        model = recebiveis
        fields = '__all__'
