from rest_framework import generics
from contas.models import Contas
from contas.serializers import ContaModelSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaulPermission

class ContaCreatListView(generics.ListCreateAPIView):
    permission_classes = ( IsAuthenticated, GlobalDefaulPermission)
    queryset = Contas.objects.all()
    serializer_class = ContaModelSerializer

class ContasRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaulPermission)
    queryset = Contas.objects.all()
    serializer_class = ContaModelSerializer