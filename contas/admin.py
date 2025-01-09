from django.contrib import admin
from contas.models import Contas

@admin.register(Contas)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('month', 'name_accounts', 'matury', 'value', 'annotation')

