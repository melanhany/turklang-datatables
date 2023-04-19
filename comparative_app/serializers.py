from rest_framework import serializers
from .models import Language, Concept, GrammaticCategory, GrammaticValue, AffixalMorpheme, RootMorpheme, RootConcept

class AffixalMorphSerializer(serializers.ModelSerializer):
    gram_value = serializers.StringRelatedField()
    class Meta:
        model = AffixalMorpheme
        fields = ['morph_name', 'gram_value']

class LanguageAffSerializer(serializers.ModelSerializer):
    affixal_morphemes = AffixalMorphSerializer(many=True)
    class Meta:
        model = Language
        fields = ['name', 'affixal_morphemes']

class RootMorphSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    class Meta:
        model = RootMorpheme
        fields = ['root_name', 'language']

class RootConceptSerializer(serializers.ModelSerializer):
    concept = serializers.StringRelatedField()
    root = RootMorphSerializer()
    class Meta:
        model = RootConcept
        fields = ['concept', 'root']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammaticCategory
        fields = ['id', 'en_name', 'ru_name']