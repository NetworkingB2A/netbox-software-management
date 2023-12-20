from netbox.filtersets import NetBoxModelFilterSet
from .models import SoftwareVersion

class SoftwareVersionFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = SoftwareVersion
        fields = ('name', 'software_hash_value', 'software_version_type')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)