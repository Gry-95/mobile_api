from django.contrib import admin
from .models import Worker, Shop, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name',)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker')
    search_fields = ('name',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'shop', 'worker', 'latitude', 'longitude')
    search_fields = ('worker__name', 'shop__name')
