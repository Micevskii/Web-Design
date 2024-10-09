from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Apartments

admin.site.register(Apartments)
class Apartments(TranslationAdmin):
    list_display = ('title', 'adress', 'small_description', 'description')