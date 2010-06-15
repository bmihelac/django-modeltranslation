from modeltranslation.translator import translator, TranslationOptions

from example.models import Product, ProductVariant


class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProductVariantTranslationOptions(TranslationOptions):
    fields = ('color',)
    

translator.register(Product, ProductTranslationOptions)
translator.register(ProductVariant, ProductVariantTranslationOptions)

# import translation.py from other apps if they provide translation registry
# import app1.translation
