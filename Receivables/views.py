from rest_framework import generics
from Receivables.models import recebiveis
from Receivables.serializers import ReceivablesSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaulPermission


class ReceivablesListViews(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaulPermission)
    queryset = recebiveis.objects.all()
    serializer_class = ReceivablesSerializer


class ReceivablesRetriveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaulPermission)
    queryset = recebiveis.objects.all()
    serializer_class = ReceivablesSerializer
