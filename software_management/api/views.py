from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import SoftwareVersionSerializer


class SoftwareVersionViewSet(NetBoxModelViewSet):
    queryset = models.SoftwareVersion.objects.prefetch_related('tags')
    serializer_class = SoftwareVersionSerializer