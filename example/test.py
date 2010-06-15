from modeltranslation.translator import translator, TranslationOptions

from example.models import Product, ProductVariant


class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProductVariantTranslationOptions(TranslationOptions):
    fields = ('color',)
    

translator.register(Product, ProductTranslationOptions)
translator.register(ProductVariant, ProductVariantTranslationOptions)
