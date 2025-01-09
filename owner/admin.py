from django.contrib import admin
from owner.models import Dono


@admin.register(Dono)
class DonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
