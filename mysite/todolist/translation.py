from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Task)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')