from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

softwareversion_buttons = [
    PluginMenuButton(
        link='plugins:software_management:softwareversion_list',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:software_management:softwareversion_list',
        link_text='Software management',
        buttons=softwareversion_buttons
    ),
)