from rest_framework_datatables.pagination import DatatablesLimitOffsetPagination

class PivotedDataPagination(DatatablesLimitOffsetPagination):
    default_limit = 10

    def get_count_and_total_count(self, queryset, view):
        if hasattr(view, '_datatables_filtered_count'):
            count = view._datatables_filtered_count
            del view._datatables_filtered_count
        else:  # pragma: no cover
            count = len(queryset)
        if hasattr(view, '_datatables_total_count'):
            total_count = view._datatables_total_count
            del view._datatables_total_count
        else:  # pragma: no cover
            total_count = count
        return count, total_count
