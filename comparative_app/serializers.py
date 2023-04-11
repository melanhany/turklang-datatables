from rest_framework import serializers
from .models import Language, Concept, GrammaticCategory, GrammaticValue, AffixalMorpheme, RootMorpheme


class ValueSerializer(serializers.ModelSerializer):
    # affixal_morphemes = SimpleAffixalSerializer(many=True)
    value_name = serializers.SerializerMethodField('join_names')
    
    class Meta:
        model = GrammaticValue
        fields = ['value_name', 'affixal_morphemes']

    def join_names (self, value):
        return f'{value.en_name} : {value.ru_name}'
        

class AffixalMorphSerializer(serializers.ModelSerializer):
    gram_value = serializers.StringRelatedField()
    class Meta:
        model = AffixalMorpheme
        fields = ['morph_name', 'gram_value']

class LanguageSerializer(serializers.ModelSerializer):
    affixal_morphemes = AffixalMorphSerializer(many=True)
    class Meta:
        model = Language
        fields = ['name', 'affixal_morphemes']

class RootMorphSerializer(serializers.ModelSerializer):
    class Meta:
        model = RootMorpheme
        fields = ['id', 'name', 'concept', 'language']

class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ['id', 'en_name', 'ru_name']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammaticCategory
        fields = ['id', 'en_name', 'ru_name']