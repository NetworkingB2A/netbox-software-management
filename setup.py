from setuptools import find_packages, setup

setup(
    name='netbox_software_management',
    version='0.1',
    description='A plugin that manages software in netbox',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)