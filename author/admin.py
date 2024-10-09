from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Author

admin.site.register(Author)
class Author(TranslationAdmin):
    list_display = ('name')