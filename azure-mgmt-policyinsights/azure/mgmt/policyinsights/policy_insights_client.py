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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.policy_events_operations import PolicyEventsOperations
from .operations.policy_states_operations import PolicyStatesOperations
from .operations.operations import Operations
from . import models


class PolicyInsightsClientConfiguration(AzureConfiguration):
    """Configuration for PolicyInsightsClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(PolicyInsightsClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-policyinsights/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class PolicyInsightsClient(object):
    """PolicyInsightsClient

    :ivar config: Configuration for client.
    :vartype config: PolicyInsightsClientConfiguration

    :ivar policy_events: PolicyEvents operations
    :vartype policy_events: azure.mgmt.policyinsights.operations.PolicyEventsOperations
    :ivar policy_states: PolicyStates operations
    :vartype policy_states: azure.mgmt.policyinsights.operations.PolicyStatesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.policyinsights.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = PolicyInsightsClientConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-12-12-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.policy_events = PolicyEventsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policy_states = PolicyStatesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
