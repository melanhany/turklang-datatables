from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AffixalMorpheme, Language, RootConcept
from .serializers import AffixalMorphSerializer, LanguageAffSerializer, RootConceptSerializer
from .pagination import PivotedDataPagination
from .filters import PivotedDataFilter
import pandas as pd
import numpy as np

class AffixalValueViewset(ListAPIView):
    queryset = Language.objects.prefetch_related('affixal_morphemes__gram_value').all()
    serializer_class = LanguageAffSerializer
    pagination_class = PivotedDataPagination
    filter_backends = [PivotedDataFilter]
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        paginator = self.pagination_class()
        filter_backend = PivotedDataFilter()

        pivoted_data = self.pivot_json(serializer.data)

        filtered_data = filter_backend.filter_queryset(request, pivoted_data, self)
        paginated_data = paginator.paginate_queryset(filtered_data, request)
        
        return paginator.get_paginated_response(paginated_data)
    
    def pivot_json(self, jsonData):
        for i, d in enumerate(jsonData):
            if not d['affixal_morphemes']:
                jsonData[i]['affixal_morphemes'] = [{'morph_name': {}, 'gram_value': {}}]
                
        df = pd.json_normalize(jsonData)
        df = pd.json_normalize(df.to_dict(orient="records"), meta=["name"], record_path="affixal_morphemes")
        df.fillna('!', inplace=True)
        df = df.groupby(['name', 'gram_value'])['morph_name'].agg(morph_name = '<br>'.join).reset_index()
        df = pd.pivot(df, values='morph_name', index='gram_value', columns='name')
        df.drop(index='!', inplace=True)
        df.replace('!', np.nan, inplace=True)
        df.replace(np.nan, '', inplace=True)
        df = df.reset_index()
        good_json = df.to_dict(orient='records')
        
        return good_json

class RootConcept(ListAPIView):
    queryset = RootConcept.objects.prefetch_related('root__language')\
                                  .prefetch_related('concept').all()
    serializer_class = RootConceptSerializer
    pagination_class = PivotedDataPagination
    filter_backends = [PivotedDataFilter]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        paginator = self.pagination_class()
        filter_backend = PivotedDataFilter()

        pivoted_data = self.pivot_json(serializer.data)

        filtered_data = filter_backend.filter_queryset(request, pivoted_data, self)
        paginated_data = paginator.paginate_queryset(filtered_data, request)
        
        return paginator.get_paginated_response(paginated_data)

    def pivot_json(self, jsonData):
        df = pd.json_normalize(jsonData)
        df = df.groupby(['concept', 'root.language'])['root.root_name'].agg(root_name='<br>'.join).reset_index()
        df = pd.pivot(df, values='root_name', index='concept', columns='root.language')
        df.replace(np.nan, '', inplace=True)
        df = df.reset_index()
        good_json = df.to_dict(orient='records')
        
        return good_json


def base(request):
    if request.get_full_path() == '/affixal-value/':
        return render(request, "comparative_app/gram_affixal_value.html")
    elif request.get_full_path() == '/root-concept/':
        return render(request, "comparative_app/root_concept.html")