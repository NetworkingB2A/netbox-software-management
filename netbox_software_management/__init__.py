from extras.plugins import PluginConfig

class NetBoxSoftwareManagement(PluginConfig):
    name = 'netbox_software_management'
    verbose_name = 'Management of software images based on devices'
    description = 'Management of software images based on devices'
    version = '0.1'
    base_url = 'software-management'

config = NetBoxSoftwareManagement