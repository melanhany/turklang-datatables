from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AffixalMorpheme, GrammaticValue
from .serializers import AffixalMorphSerializer, ValueSerializer
from .pagination import PivotedDataPagination
import pandas as pd
import numpy as np

class GrammaticValueViewset(APIView):
    serializer_class = ValueSerializer
    pagination_class = PivotedDataPagination

    def get(self, request):
        queryset = GrammaticValue.objects.prefetch_related('affixal_morphemes__language').all()
        paginator = self.pagination_class()

        serializer = self.serializer_class(queryset, many=True)
        pivoted_data = GrammaticValueViewset.pivot_json(serializer.data)
        
        paginated_data = paginator.paginate_queryset(pivoted_data, request)

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

    return render(request, "comparative_app/base.html")