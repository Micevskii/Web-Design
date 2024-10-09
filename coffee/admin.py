from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Coffee

admin.site.register(Coffee)
class Coffee(TranslationAdmin):
    list_display = ('title', 'adress', 'small_description', 'description')