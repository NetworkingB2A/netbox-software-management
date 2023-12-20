from netbox.forms import NetBoxModelForm
from .models import SoftwareVersion

class SoftwareVersionForm(NetBoxModelForm)
    comments = CommentField()
    
    class Meta:
        model = SoftwareVersion
        fields = ('name', 'software_version_type', 'software_hash_value',  'description', 'comments', 'tags')

