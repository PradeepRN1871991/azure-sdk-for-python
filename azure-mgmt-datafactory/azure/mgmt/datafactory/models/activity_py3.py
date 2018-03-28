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


class Activity(Model):
    """A pipeline activity.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ExecutionActivity, ControlActivity

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Execution': 'ExecutionActivity', 'Container': 'ControlActivity'}
    }

    def __init__(self, *, name: str, additional_properties=None, description: str=None, depends_on=None, **kwargs) -> None:
        super(Activity, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.name = name
        self.description = description
        self.depends_on = depends_on
        self.type = None
