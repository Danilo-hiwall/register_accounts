from django.urls import path
from . import views

urlpatterns = [

    path('cartao/', views.CartaoCreatListView.as_view(), name='cartao-create-list'),
    path('cartao/<int:pk>', views.CartaoRetriveUpdateDestroyViews.as_view(), name='cartao-detail-view'),
]