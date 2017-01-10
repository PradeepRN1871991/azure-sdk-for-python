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

from .resource import Resource


class MediaService(Resource):
    """The properties of a Media Service resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource
    :vartype type: str
    :param location: The geographic location of the resource. This must be one
     of the supported and registered Azure Geo Regions (for example, West US,
     East US, Southeast Asia, and so forth).
    :type location: str
    :param tags: Tags to help categorize the resource in the Azure portal.
    :type tags: dict
    :ivar api_endpoints: Read-only property that lists the Media Services REST
     API endpoints for this resource. If supplied on a PUT or PATCH, the value
     will be ignored.
    :vartype api_endpoints: list of :class:`ApiEndpoint
     <azure.mgmt.media.models.ApiEndpoint>`
    :param storage_accounts: The storage accounts for this resource.
    :type storage_accounts: list of :class:`StorageAccount
     <azure.mgmt.media.models.StorageAccount>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'api_endpoints': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'api_endpoints': {'key': 'properties.apiEndpoints', 'type': '[ApiEndpoint]'},
        'storage_accounts': {'key': 'properties.storageAccounts', 'type': '[StorageAccount]'},
    }

    def __init__(self, location=None, tags=None, storage_accounts=None):
        super(MediaService, self).__init__(location=location, tags=tags)
        self.api_endpoints = None
        self.storage_accounts = storage_accounts