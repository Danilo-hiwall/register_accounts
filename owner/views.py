from rest_framework import generics
from owner.models import Dono
from owner.serializers import DonoModelSerializer

class DonoCreatListView(generics.ListCreateAPIView):
    queryset = Dono.objects.all()
    serializer_class = DonoModelSerializer

class DonoRetriveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dono.objects.all()
    serializer_class = DonoModelSerializer
