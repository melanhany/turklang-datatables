from django.contrib import admin
from .models import AffixalMorpheme
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.
@admin.register(AffixalMorpheme)
class AffixalMorphemeAdmin(admin.ModelAdmin):
    search_fields = ['morph_name']



