from rest_framework import serializers
from owner.models import Dono

class DonoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dono
        fields = '__all__'