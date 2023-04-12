from django.shortcuts import render
from rest_framework_datatables.filters import DatatablesFilterBackend
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet
from rest_framework_datatables.renderers import DatatablesRenderer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AffixalMorpheme, GrammaticValue, Language
from .serializers import AffixalMorphSerializer, ValueSerializer, LanguageSerializer
from .pagination import PivotedDataPagination
from .filters import PivotedDataFilter
import pandas as pd
import numpy as np

class LanguagePivotViewset(ListAPIView):
    queryset = Language.objects.prefetch_related('affixal_morphemes__gram_value').all()
    serializer_class = LanguageSerializer
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

class GrammaticValueViewset(APIView):
    serializer_class = ValueSerializer
    pagination_class = PivotedDataPagination

    def get(self, request):
        queryset = GrammaticValue.objects.prefetch_related('affixal_morphemes__language').all()
        paginator = self.pagination_class()
        
        serializer = self.serializer_class(queryset, many=True)
        pivoted_data = GrammaticValueViewset.pivot_json(serializer.data)

        paginated_data = paginator.paginate_queryset(pivoted_data, request)
        
        # paginated_data = paginator.get_count_and_total_count(pivoted_data, GrammaticValueViewset)

        return paginator.get_paginated_response(paginated_data)

    
    def pivot_json(data):
        json = data
        for i, d in enumerate(json):
            if not d['affixal_morphemes']:
                json[i]['affixal_morphemes'] = [{'name': {}, 'language': {}}]
        
        df = pd.json_normalize(json)
        df = pd.json_normalize(df.to_dict(orient="records"), meta=["value_name"], record_path="affixal_morphemes", record_prefix="affixal_")
        df.fillna('!', inplace=True)
        df = df.groupby(['value_name', 'affixal_language'], dropna=False)['affixal_name'].agg(affixal_name = '\n'.join).reset_index()

        df = pd.pivot(df, values='affixal_name', index='value_name', columns='affixal_language')
        df.drop(columns='!', inplace=True)
        df.replace('!', np.nan, inplace=True)
        df.replace(np.nan, '', inplace=True)
        df = df.reset_index()
        good_json = df.to_dict(orient='records')
        
        return good_json

class GrammaticAffixalViewset(APIView):
    serializer_class = AffixalMorphSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = AffixalMorpheme.objects. \
                    prefetch_related("language", "gram_value").all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    

def base(request):

    return render(request, "comparative_app/gram_affixal_value.html")