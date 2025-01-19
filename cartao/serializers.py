from rest_framework import serializers
from cartao.models import Cartao
from owner.serializers import DonoModelSerializer


class CartaoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cartao
        fields = '__all__'

class CartaoListDetailSerializer(serializers.ModelSerializer):
    owner = DonoModelSerializer(many=True)

    class Meta:
        model = Cartao
        fields = ['id', 'type_card', 'owner', 'closing', 'matury', 'limit_card']