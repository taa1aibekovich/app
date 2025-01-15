from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Store)
class ProductTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description')


@register(Contact)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')


@register(Combo)
class ProductTranslationOptions(TranslationOptions):
    fields = ('combo_name', 'description')


@register(CarItem)
class ProductTranslationOptions(TranslationOptions):
    fields = ('combo',)


@register(StoreReview)
class ProductTranslationOptions(TranslationOptions):
    fields = ('text',)
