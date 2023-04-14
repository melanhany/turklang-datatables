from django.db import models

class Language(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Concept(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    en_name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)

class GrammaticCategory(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    en_name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)

class GrammaticValue(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    #sec_id = models.BigIntegerField(unique=True, null=True)
    en_name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)
    category = models.ForeignKey(GrammaticCategory, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.en_name} : {self.ru_name}'
class AffixalMorpheme(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    morph_name = models.CharField(max_length=255)
    #allomorph = models.CharField(max_length=255)
    gram_value = models.ForeignKey(GrammaticValue, to_field='id', on_delete=models.CASCADE, null=True, related_name='affixal_morphemes')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='affixal_morphemes')

    def __str__(self) -> str:
        return self.morph_name

class RootMorpheme(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    