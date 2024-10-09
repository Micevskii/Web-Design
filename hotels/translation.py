from modeltranslation.translator import register, TranslationOptions
from .models import Hotels

@register(Hotels)
class Hotels(TranslationOptions):
    fields = ('title', 'adress', 'small_description', 'description')  # Fields you want to translate
