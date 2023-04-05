from django.urls import path
from .views import GrammaticAffixalViewset, GrammaticValueViewset
from rest_framework.routers import DefaultRouter

urlpatterns = [
        path('grammatic-value/', GrammaticValueViewset.as_view()),
        path('grammatic-affixal/', GrammaticAffixalViewset.as_view()),
]

