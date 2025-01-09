from django.urls import path
from . import views

urlpatterns = [

    path('contas/', views.ContaCreatListView.as_view(), name='contas-creat-list'),
    path('contas/<int:pk>', views.ContasRetriveUpdateDestroyView.as_view(), name='contas-detail-view'),
]
