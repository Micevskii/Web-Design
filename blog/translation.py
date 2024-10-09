from modeltranslation.translator import register, TranslationOptions
from .models import Blogs

@register(Blogs)
class Blog(TranslationOptions):
     fields = ('title', 'category', 'description')

