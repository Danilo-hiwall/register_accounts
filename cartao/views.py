from rest_framework import generics
from cartao.models import Cartao
from cartao.serializers import CartaoModelSerializer


class CartaoCreatListView(generics.ListCreateAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoModelSerializer

class CartaoRetriveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cartao.objects.all()
    serializer_class = CartaoModelSerializer


