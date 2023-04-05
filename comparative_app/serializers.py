from rest_framework import serializers
from .models import Language, Concept, GrammaticCategory, GrammaticValue, AffixalMorpheme, RootMorpheme

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']
    
class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ['id', 'en_name', 'ru_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammaticCategory
        fields = ['id', 'en_name', 'ru_name']

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammaticValue
        fields = ['ru_name']

class AffixalMorphSerializer(serializers.ModelSerializer):
    gram_value = ValueSerializer()
    language = LanguageSerializer()
    class Meta:
        model = AffixalMorpheme
        fields = ['id', 'name', 'gram_value', 'language']

class RootMorphSerializer(serializers.ModelSerializer):
    class Meta:
        model = RootMorpheme
        fields = ['id', 'name', 'concept', 'language']