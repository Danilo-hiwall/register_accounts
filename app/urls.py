from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('cartao.urls')),

    path('api/v1/', include('contas.urls')),
    
    path('api/v1/', include('owner.urls')),




]
