from modeltranslation.translator import register, TranslationOptions
from .models import Restaurants

@register(Restaurants)
class Restaurants(TranslationOptions):
    fields = ('title', 'adress', 'small_description', 'description')  # Fields you want to translate
