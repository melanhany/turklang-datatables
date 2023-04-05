from django.urls import path
from .views import GrammaticAffixalViewset, GrammaticValueViewset
from rest_framework.routers import DefaultRouter

urlpatterns = [
        path('val/', GrammaticValueViewset.as_view()),
        path('aff/', GrammaticAffixalViewset.as_view()),
]

