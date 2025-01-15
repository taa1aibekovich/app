
from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Category,Store, Contact, Product, Combo, CarItem, StoreReview)
class ProductAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
# admin.site.register(Category)
# admin.site.register(Store)
# admin.site.register(Contact)
# admin.site.register(Product)
# admin.site.register(Combo)
admin.site.register(Cart)
# admin.site.register(CarItem)
admin.site.register(Order)
admin.site.register(Courier)
# admin.site.register(StoreReview)
admin.site.register(CourierRating)

