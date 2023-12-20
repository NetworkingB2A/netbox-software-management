from extras.plugins import PluginConfig

class NetBoxSoftwareManagement(PluginConfig):
    name = 'software_management'
    verbose_name = 'Software Management'
    description = 'Management of software images based on devices'
    version = '0.1'
    base_url = 'software-management'

config = NetBoxSoftwareManagement