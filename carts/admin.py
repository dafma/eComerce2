from django.contrib import admin

# Register your models here.
from .models import CartItem, Cart

class CartItemInline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]

    class Meta:
        model = Cart