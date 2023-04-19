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

class RootMorphSerializer(serializers.ModelSerializer):
    concept = serializers.StringRelatedField()

    class Meta:
        model = RootMorpheme
        fields = ['root_name', 'concept']

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

class LanguageRootSerializer(serializers.ModelSerializer):
    root_morphemes = RootMorphSerializer(many=True)

    class Meta:
        model = Language
        fields = ['name', 'root_morphemes']

class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ['id', 'en_name', 'ru_name']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammaticCategory
        fields = ['id', 'en_name', 'ru_name']