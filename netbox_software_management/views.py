from netbox.views import generic
from . import forms, models, tables



class SoftwareVersionView(generic.ObjectView):
    queryset = models.SoftwareVersion.objects.all()
    
class SoftwareVersionListView(generic.ObjectListView):
    queryset = models.SoftwareVersion.objects.all()
    table = tables.SoftwareVersionTable

class SoftwareVersionEditView(generic.ObjectEditView):
    queryset = models.SoftwareVersion.objects.all()
    form = forms.SoftwareVersionForm

class SoftwareVersionDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareVersion.objects.all()