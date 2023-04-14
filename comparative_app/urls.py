from django.urls import path
from .views import GrammaticAffixalViewset, AffixalValueViewset, base

urlpatterns = [
        path('api/grammatic-affixal/', GrammaticAffixalViewset.as_view()),
        path('api/affixal-value/', AffixalValueViewset.as_view()),
        path('index/', base)
]

