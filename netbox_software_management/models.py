from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

# Firmware, linux, Versa, Cisco
class SoftwareTypeChoices(ChoiceSet):
    key = 'SoftwareVersionRule.action'

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
    default_action = models.CharField(
        max_length=30
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        # This is to order the software version by name. by default this is ordered by ID number.
        ordering = ('name',)

    def __str__(self):
        return self.name
    


# I will set up a version of there I set the status of a image.
# Firmware, linux, Versa, Cisco
# field called hash
class SoftwareVersionRule(NetBoxModel):
    software_version = models.ForeignKey(
        to=SoftwareVersion,
        on_delete=models.CASCADE,
        related_name='software'
    )
    # This i am not positive will work how i want it to. So I will comment it out for now. I still want to write it because I do want this.
    # device_type = models.ForeignKey(
    #     to='dcim.device-types',
    #     on_delete=models.PROTECT,
    #     related_name='+',
    #     blank=True,
    #     null=True
    # )
    description = models.CharField(
        max_length=500,
        blank=True
    )

    software_hash_value = models.CharField(
        max_length=125,
        blank=True
    )

    software_version_type = models.CharField(
        max_length=30,
        choices=SoftwareTypeChoices
    )

    class Meta:
        ordering = ('software_version',)
        unique_together = ('software_version',)

    def __str__(self):
        return f'{self.software_version}'

    def get_software_version_type_color(self):
        return SoftwareTypeChoices.colors.get(self.software_version_type)