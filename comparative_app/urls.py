from django.urls import path
from .views import AffixalValueViewset, RootConcept, base

urlpatterns = [
        path('api/affixal-value/', AffixalValueViewset.as_view()),
        path('api/root-concept/', RootConcept.as_view()),
        path('affixal-value/', base),
        path('root-concept/', base)
]

