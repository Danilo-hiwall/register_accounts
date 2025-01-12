from rest_framework import serializers
from cartao.models import Cartao


class CartaoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cartao
        fields = '__all__'
