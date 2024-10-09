from modeltranslation.translator import register, TranslationOptions
from .models import Buildings

@register(Buildings)
class Buildings(TranslationOptions):
    fields = ('title', 'adress', 'small_description', 'description')  # Fields you want to translate
