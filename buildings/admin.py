from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Buildings

admin.site.register(Buildings)
class Buildings(TranslationAdmin):
    list_display = ('title', 'adress', 'small_description', 'description')