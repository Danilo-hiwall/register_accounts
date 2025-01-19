from django.urls import path
from . import views

urlpatterns = [

    path('receivables/', views.ReceivablesListViews.as_view(), name='receivables-create-views'),
    path('receivables/<int:pk>', views.ReceivablesRetriveUpdateDestroyViews.as_view(), name='receivables-datail-view'),
]
