from django.urls import path
from .views import GrammaticAffixalViewset, GrammaticValueViewset, base

urlpatterns = [
        path('grammatic-value/', GrammaticValueViewset.as_view()),
        path('grammatic-affixal/', GrammaticAffixalViewset.as_view()),
        path('index/', base)
]

