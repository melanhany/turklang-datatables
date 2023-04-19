from django.urls import path
from .views import GrammaticAffixalViewset, AffixalValueViewset, RootConcept, base

urlpatterns = [
        path('api/affixal-value/', AffixalValueViewset.as_view()),
        path('api/root-concept/', RootConcept.as_view()),
        path('index/', base)
]

