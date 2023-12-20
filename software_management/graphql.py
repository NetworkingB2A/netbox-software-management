from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models


class SoftwareVersionType(NetBoxObjectType):

    class Meta:
        model = models.SoftwareVersion
        fields = '__all__'

class Query(ObjectType):
    software_version = ObjectField(SoftwareVersionType)
    software_version_list = ObjectListField(SoftwareVersionType)
    
schema = Query