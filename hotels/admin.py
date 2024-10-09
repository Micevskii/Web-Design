from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Hotels

admin.site.register(Hotels)
class Hotels(TranslationAdmin):
    list_display = ('title', 'adress', 'small_description', 'description')