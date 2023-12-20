from netbox.search import SearchIndex, register_search
from .models import SoftwareVersion

@register_search
class SoftwareVersionIndex(SearchIndex):
    model = SoftwareVersion
    fields = (
        ('name', 100),
        ('software_hash_value', 500),
        ('comments', 5000),
    )