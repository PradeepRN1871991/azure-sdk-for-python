# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Container(Model):
    """A container instance.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The user-provided name of the container instance.
    :type name: str
    :param image: Required. The name of the image used to create the container
     instance.
    :type image: str
    :param command: The commands to execute within the container instance in
     exec form.
    :type command: list[str]
    :param ports: The exposed ports on the container instance.
    :type ports: list[~azure.mgmt.containerinstance.models.ContainerPort]
    :param environment_variables: The environment variables to set in the
     container instance.
    :type environment_variables:
     list[~azure.mgmt.containerinstance.models.EnvironmentVariable]
    :ivar instance_view: The instance view of the container instance. Only
     valid in response.
    :vartype instance_view:
     ~azure.mgmt.containerinstance.models.ContainerPropertiesInstanceView
    :param resources: Required. The resource requirements of the container
     instance.
    :type resources: ~azure.mgmt.containerinstance.models.ResourceRequirements
    :param volume_mounts: The volume mounts available to the container
     instance.
    :type volume_mounts:
     list[~azure.mgmt.containerinstance.models.VolumeMount]
    """

    _validation = {
        'name': {'required': True},
        'image': {'required': True},
        'instance_view': {'readonly': True},
        'resources': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'image': {'key': 'properties.image', 'type': 'str'},
        'command': {'key': 'properties.command', 'type': '[str]'},
        'ports': {'key': 'properties.ports', 'type': '[ContainerPort]'},
        'environment_variables': {'key': 'properties.environmentVariables', 'type': '[EnvironmentVariable]'},
        'instance_view': {'key': 'properties.instanceView', 'type': 'ContainerPropertiesInstanceView'},
        'resources': {'key': 'properties.resources', 'type': 'ResourceRequirements'},
        'volume_mounts': {'key': 'properties.volumeMounts', 'type': '[VolumeMount]'},
    }

    def __init__(self, *, name: str, image: str, resources, command=None, ports=None, environment_variables=None, volume_mounts=None, **kwargs) -> None:
        super(Container, self).__init__(**kwargs)
        self.name = name
        self.image = image
        self.command = command
        self.ports = ports
        self.environment_variables = environment_variables
        self.instance_view = None
        self.resources = resources
        self.volume_mounts = volume_mounts
