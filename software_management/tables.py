import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import SoftwareVersion

class SoftwareVersionTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    
    software_version_type = ChoiceFieldColumn()
    class Meta(NetBoxTable.Meta):
        model = SoftwareVersion
        fields = ('pk','name','software_version_type','software_hash_value', 'description', 'comments', 'actions')
        default_columns = ('name', 'software_version_type', 'software_hash_value')