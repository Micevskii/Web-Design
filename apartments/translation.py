from modeltranslation.translator import register, TranslationOptions
from .models import Apartments

@register(Apartments)
class Apartments(TranslationOptions):
    fields = ('title', 'adress', 'small_description', 'description')  # Fields you want to translate
