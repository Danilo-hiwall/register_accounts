from rest_framework import generics, views, response
from cartao.models import Cartao
from cartao.serializers import CartaoModelSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaulPermission
from django.db.models import Sum
from cartao.serializers import CartaoListDetailSerializer

class CartaoCreatListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaulPermission)
    queryset = Cartao.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CartaoListDetailSerializer
        return CartaoModelSerializer

class CartaoRetriveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaulPermission)
    queryset = Cartao.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CartaoListDetailSerializer
        return CartaoModelSerializer



class CardLimit(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaulPermission)
    queryset = Cartao.objects.all()
    

    def get(self, request):
        # Calcula o limite total dos cartões
        total_limit = Cartao.objects.aggregate(total_limit=Sum('limit_card'))['total_limit']
        total_limit = total_limit if total_limit is not None else 0.0
        
        return response.Response({"total_limit": total_limit})