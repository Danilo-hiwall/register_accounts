from django.contrib import admin
from cartao.models import Cartao

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ('type_card', 'closing', 'matury', 'limit_card')