from django.contrib import admin

# Register your models here.
from .models import Product, Variation, ProductImage, Category, ProductFeatured


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price']
    inlines = [
        VariationInline,
        ProductImageInline
    ]

    class Meta:
        model = Product



admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductFeatured)



