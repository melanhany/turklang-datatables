from rest_framework.filters import BaseFilterBackend
from rest_framework_datatables.filters import DatatablesFilterBackend
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet

class PivotedDataFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):        
        params = request.query_params
        for param in params:
            if param.startswith('search[value]'):
                search_term = params.get(param)
                queryset = [data for data in queryset \
                            if any(search_term in term \
                                   for term in data.values())]
            elif param.startswith('order'):
                order_column_index = int(params.get(f'order[0][column]'))
                order_direction = str(params.get(f'order[0][dir]'))
                if order_direction == 'asc':
                    queryset = sorted(queryset, key=lambda d: list(d.values())[order_column_index])
                else:
                    queryset = sorted(queryset, key=lambda d: list(d.values())[order_column_index], reverse=True)

        return queryset
