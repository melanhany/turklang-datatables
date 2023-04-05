from django.shortcuts import render
from django_pivot.pivot import pivot
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AffixalMorpheme, GrammaticValue
from .serializers import AffixalMorphSerializer, ValueSerializer

class GrammaticValueViewset(APIView):
    serializer_class = ValueSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = GrammaticValue.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class GrammaticAffixalViewset(APIView):
    serializer_class = AffixalMorphSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = AffixalMorpheme.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
