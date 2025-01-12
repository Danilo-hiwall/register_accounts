from rest_framework import generics
from owner.models import Dono
from owner.serializers import DonoModelSerializer
from rest_framework.permissions import IsAuthenticated

class DonoCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Dono.objects.all()
    serializer_class = DonoModelSerializer

class DonoRetriveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Dono.objects.all()
    serializer_class = DonoModelSerializer
