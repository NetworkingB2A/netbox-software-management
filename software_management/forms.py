from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import SoftwareVersion

class SoftwareVersionForm(NetBoxModelForm):
    comments = CommentField()
    
    class Meta:
        model = SoftwareVersion
        fields = ('name', 'software_version_type', 'software_hash_value',  'description', 'comments', 'tags')

