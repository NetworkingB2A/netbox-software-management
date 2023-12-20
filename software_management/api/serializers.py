from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import SoftwareVersion

class NestedAccessListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:software_management-api:softwareversion-detail'
    )

    class Meta:
        model = SoftwareVersion
        fields = ('id', 'url', 'display', 'name')

class SoftwareVersionSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:software_management-api:softwareversion-detail'
    )

    class Meta:
        model = SoftwareVersion
        fields = fields = ('id', 'url', 'display', 'name', 'software_hash_value', 'software_version_type', 'description',  'comments', 'tags', 'custom_fields', 'created',
            'last_updated')