from rest_framework import generics
from contas.models import Contas
from contas.serializers import ContaModelSerializer


class ContaCreatListView(generics.ListCreateAPIView):
    queryset = Contas.objects.all()
    serializer_class = ContaModelSerializer

class ContasRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contas.objects.all()
    serializer_class = ContaModelSerializer