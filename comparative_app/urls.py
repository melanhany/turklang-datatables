from django.urls import path
from .views import GrammaticAffixalViewset, GrammaticValueViewset, LanguagePivotViewset, base

urlpatterns = [
        path('grammatic-affixal/', GrammaticAffixalViewset.as_view()),
        path('language/', LanguagePivotViewset.as_view()),
        path('index/', base)
]

