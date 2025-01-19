from rest_framework import serializers
from Receivables.models import recebiveis
from owner.serializers import DonoModelSerializer
from django.db.models import Sum


class ReceivablesSerializer(serializers.ModelSerializer):

    class Meta:
        model = recebiveis
        fields = '__all__'

class ReceivablesDetailSerializer(serializers.ModelSerializer):
    entries_of = DonoModelSerializer(many=True)
    all_entries = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = recebiveis
        fields = ['entry_date', 'entries_of', 'value', 'Depositor', 'payment_method', 'resume', 'all_entries']

    def get_all_entries(self, obj):
        from django.db.models import Sum

        
        total = recebiveis.objects.aggregate(total_value=Sum('value'))['total_value']
        return total or 0  