from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Blogs

admin.site.register(Blogs)
class Blog(TranslationAdmin):
    list_display = ('title', 'category', 'description')