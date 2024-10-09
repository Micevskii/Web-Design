from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Restaurants

admin.site.register(Restaurants)
class Restaurants(TranslationAdmin):
    list_display = ('title', 'adress', 'small_description', 'description')