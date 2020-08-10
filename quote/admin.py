from django.contrib import admin

from .models import Quote, Shopping

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'luggage_type', 'luggage_weight', 'luggage_dimensions', 'origin', 'destination', 'mode', 'date', 'complete']

@admin.register(Shopping)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'description']
