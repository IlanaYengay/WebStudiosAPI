from django.contrib import admin
from .models import Order, Image
from .tasks import process_order


def set_orders_to_processing(modeladmin, request, queryset):
    for order in queryset:
        process_order.delay(order.id)


set_orders_to_processing.short_description = "Отправить на обработку"


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'title', 'user', 'status']
    ordering = ['order_number']
    actions = [set_orders_to_processing]


admin.site.register(Order, OrderAdmin)
admin.site.register(Image)
