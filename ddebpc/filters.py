import django_filters
from.models import DdeBpc


class DdeBpcFiltre(django_filters.FilterSet):
    class Meta:
        model = DdeBpc
        fields = 'personnel', 'relation', 'ayantdroit'
