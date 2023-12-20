from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import SoftwareVersion, SoftwareTypeChoices

class SoftwareVersionForm(NetBoxModelForm):
    comments = CommentField()
    
    class Meta:
        model = SoftwareVersion
        fields = ('name', 'software_version_type', 'software_hash_value',  'description', 'comments', 'tags')

class SoftwareVersionFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareVersion
    
    SoftwareVersion = forms.ModelMultipleChoiceField(
        queryset=SoftwareVersion.objects.all(),
        required=False
    )
    
    software_types = forms.MultipleChoiceField(
        choices=SoftwareTypeChoices,
        required=False
    )
    
    # Couldn't get this filter to work, I will need to look to see how its done.
    # hash_value = forms.CharField(
    #     queryset=SoftwareVersion.objects.all(),
    #     required=False
    # )