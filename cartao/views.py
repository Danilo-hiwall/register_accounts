from rest_framework import generics
from cartao.models import Cartao
from cartao.serializers import CartaoModelSerializer
from rest_framework.permissions import IsAuthenticated


class CartaoCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cartao.objects.all()
    serializer_class = CartaoModelSerializer

class CartaoRetriveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cartao.objects.all()
    serializer_class = CartaoModelSerializer


