from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from models import Product, ProductVariant


class ProductVariantInline(TranslationTabularInline):
    model = ProductVariant
    extra = 0
    
    
class ProductAdmin(TranslationAdmin):
    inlines = (
        ProductVariantInline, 
    )


admin.site.register(Product, ProductAdmin)
