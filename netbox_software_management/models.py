from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

# Firmware, linux, Versa, Cisco
class SoftwareTypeChoices(ChoiceSet):

    CHOICES = [
        ('firmware', 'Firmware', 'green'),
        ('linux', 'linux', 'red'),
        ('versa', 'Versa', 'orange'),
        ('cisco', 'Cisco', 'blue'),
    ]

class SoftwareVersion(NetBoxModel):
    # These are the field I will see in the Gui, as well as the fields in the database.
    name = models.CharField(
    max_length=100
    )

    software_version_type = models.CharField(
        max_length=30,
        choices=SoftwareTypeChoices
    )

    software_hash_value = models.CharField(
        max_length=125,
        blank=True
    )

    description = models.CharField(
        max_length=500,
        blank=True
    )

    comments = models.TextField(
        blank=True
    )
    class Meta:
        # This is to order the software version by name. by default this is ordered by ID number.
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_software_version_type_color(self):
        return SoftwareTypeChoices.colors.get(self.software_version_type)
