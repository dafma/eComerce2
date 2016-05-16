from django.contrib import admin

# Register your models here.
from .models import Product, Variation, ProductImage, Category, ProductFeatured


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    max_num = 10


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0
    # numero maximo de  inlines
    max_num = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "price", ]
    inlines = [
        ProductImageInline,
        VariationInline
    ]

    class Meta:
        model = Product


@admin.register(Category)
class CategoryAdmi(admin.ModelAdmin):
    pass


@admin.register(ProductFeatured)
class ProductFeatured(admin.ModelAdmin):
    pass
