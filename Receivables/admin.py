from django.contrib import admin
from Receivables.models import recebiveis


@admin.register(recebiveis)
class ReceivablesAdmin(admin.ModelAdmin):
    list_display = ('entry_date', 'value', 'Depositor', 'payment_method', 'resume')
