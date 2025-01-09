from django.urls import path
from . import views

urlpatterns = [

    path('owner/',views.DonoCreatListView.as_view(), name='owner-creat-list'),
    path('owner/<int:pk>', views.DonoRetriveUpdateDestroyViews.as_view(), name='owner-detail-view'),
]