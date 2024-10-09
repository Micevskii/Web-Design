from modeltranslation.translator import register, TranslationOptions
from .models import Coffee

@register(Coffee)
class Coffee(TranslationOptions):
    fields = ('title', 'adress', 'small_description', 'description')  # Fields you want to translate
