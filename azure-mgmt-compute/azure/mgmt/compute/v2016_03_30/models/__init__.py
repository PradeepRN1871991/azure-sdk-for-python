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

try:
    from .instance_view_status_py3 import InstanceViewStatus
    from .sub_resource_py3 import SubResource
    from .availability_set_py3 import AvailabilitySet
    from .virtual_machine_size_py3 import VirtualMachineSize
    from .virtual_machine_extension_image_py3 import VirtualMachineExtensionImage
    from .virtual_machine_image_resource_py3 import VirtualMachineImageResource
    from .virtual_machine_extension_instance_view_py3 import VirtualMachineExtensionInstanceView
    from .virtual_machine_extension_py3 import VirtualMachineExtension
    from .purchase_plan_py3 import PurchasePlan
    from .os_disk_image_py3 import OSDiskImage
    from .data_disk_image_py3 import DataDiskImage
    from .virtual_machine_image_py3 import VirtualMachineImage
    from .usage_name_py3 import UsageName
    from .usage_py3 import Usage
    from .virtual_machine_capture_parameters_py3 import VirtualMachineCaptureParameters
    from .virtual_machine_capture_result_py3 import VirtualMachineCaptureResult
    from .plan_py3 import Plan
    from .hardware_profile_py3 import HardwareProfile
    from .image_reference_py3 import ImageReference
    from .key_vault_secret_reference_py3 import KeyVaultSecretReference
    from .key_vault_key_reference_py3 import KeyVaultKeyReference
    from .disk_encryption_settings_py3 import DiskEncryptionSettings
    from .virtual_hard_disk_py3 import VirtualHardDisk
    from .os_disk_py3 import OSDisk
    from .data_disk_py3 import DataDisk
    from .storage_profile_py3 import StorageProfile
    from .additional_unattend_content_py3 import AdditionalUnattendContent
    from .win_rm_listener_py3 import WinRMListener
    from .win_rm_configuration_py3 import WinRMConfiguration
    from .windows_configuration_py3 import WindowsConfiguration
    from .ssh_public_key_py3 import SshPublicKey
    from .ssh_configuration_py3 import SshConfiguration
    from .linux_configuration_py3 import LinuxConfiguration
    from .vault_certificate_py3 import VaultCertificate
    from .vault_secret_group_py3 import VaultSecretGroup
    from .os_profile_py3 import OSProfile
    from .network_interface_reference_py3 import NetworkInterfaceReference
    from .network_profile_py3 import NetworkProfile
    from .boot_diagnostics_py3 import BootDiagnostics
    from .diagnostics_profile_py3 import DiagnosticsProfile
    from .virtual_machine_extension_handler_instance_view_py3 import VirtualMachineExtensionHandlerInstanceView
    from .virtual_machine_agent_instance_view_py3 import VirtualMachineAgentInstanceView
    from .disk_instance_view_py3 import DiskInstanceView
    from .boot_diagnostics_instance_view_py3 import BootDiagnosticsInstanceView
    from .virtual_machine_identity_py3 import VirtualMachineIdentity
    from .virtual_machine_instance_view_py3 import VirtualMachineInstanceView
    from .virtual_machine_py3 import VirtualMachine
    from .sku_py3 import Sku
    from .upgrade_policy_py3 import UpgradePolicy
    from .virtual_machine_scale_set_identity_py3 import VirtualMachineScaleSetIdentity
    from .virtual_machine_scale_set_os_profile_py3 import VirtualMachineScaleSetOSProfile
    from .virtual_machine_scale_set_os_disk_py3 import VirtualMachineScaleSetOSDisk
    from .virtual_machine_scale_set_storage_profile_py3 import VirtualMachineScaleSetStorageProfile
    from .api_entity_reference_py3 import ApiEntityReference
    from .virtual_machine_scale_set_ip_configuration_py3 import VirtualMachineScaleSetIPConfiguration
    from .virtual_machine_scale_set_network_configuration_py3 import VirtualMachineScaleSetNetworkConfiguration
    from .virtual_machine_scale_set_network_profile_py3 import VirtualMachineScaleSetNetworkProfile
    from .virtual_machine_scale_set_extension_py3 import VirtualMachineScaleSetExtension
    from .virtual_machine_scale_set_extension_profile_py3 import VirtualMachineScaleSetExtensionProfile
    from .virtual_machine_scale_set_vm_profile_py3 import VirtualMachineScaleSetVMProfile
    from .virtual_machine_scale_set_py3 import VirtualMachineScaleSet
    from .virtual_machine_scale_set_vm_instance_ids_py3 import VirtualMachineScaleSetVMInstanceIDs
    from .virtual_machine_scale_set_vm_instance_required_ids_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
    from .virtual_machine_status_code_count_py3 import VirtualMachineStatusCodeCount
    from .virtual_machine_scale_set_instance_view_statuses_summary_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
    from .virtual_machine_scale_set_vm_extensions_summary_py3 import VirtualMachineScaleSetVMExtensionsSummary
    from .virtual_machine_scale_set_instance_view_py3 import VirtualMachineScaleSetInstanceView
    from .virtual_machine_scale_set_sku_capacity_py3 import VirtualMachineScaleSetSkuCapacity
    from .virtual_machine_scale_set_sku_py3 import VirtualMachineScaleSetSku
    from .virtual_machine_scale_set_vm_py3 import VirtualMachineScaleSetVM
    from .virtual_machine_scale_set_vm_instance_view_py3 import VirtualMachineScaleSetVMInstanceView
    from .api_error_base_py3 import ApiErrorBase
    from .inner_error_py3 import InnerError
    from .api_error_py3 import ApiError
    from .compute_long_running_operation_properties_py3 import ComputeLongRunningOperationProperties
    from .resource_py3 import Resource
    from .operation_status_response_py3 import OperationStatusResponse
except (SyntaxError, ImportError):
    from .instance_view_status import InstanceViewStatus
    from .sub_resource import SubResource
    from .availability_set import AvailabilitySet
    from .virtual_machine_size import VirtualMachineSize
    from .virtual_machine_extension_image import VirtualMachineExtensionImage
    from .virtual_machine_image_resource import VirtualMachineImageResource
    from .virtual_machine_extension_instance_view import VirtualMachineExtensionInstanceView
    from .virtual_machine_extension import VirtualMachineExtension
    from .purchase_plan import PurchasePlan
    from .os_disk_image import OSDiskImage
    from .data_disk_image import DataDiskImage
    from .virtual_machine_image import VirtualMachineImage
    from .usage_name import UsageName
    from .usage import Usage
    from .virtual_machine_capture_parameters import VirtualMachineCaptureParameters
    from .virtual_machine_capture_result import VirtualMachineCaptureResult
    from .plan import Plan
    from .hardware_profile import HardwareProfile
    from .image_reference import ImageReference
    from .key_vault_secret_reference import KeyVaultSecretReference
    from .key_vault_key_reference import KeyVaultKeyReference
    from .disk_encryption_settings import DiskEncryptionSettings
    from .virtual_hard_disk import VirtualHardDisk
    from .os_disk import OSDisk
    from .data_disk import DataDisk
    from .storage_profile import StorageProfile
    from .additional_unattend_content import AdditionalUnattendContent
    from .win_rm_listener import WinRMListener
    from .win_rm_configuration import WinRMConfiguration
    from .windows_configuration import WindowsConfiguration
    from .ssh_public_key import SshPublicKey
    from .ssh_configuration import SshConfiguration
    from .linux_configuration import LinuxConfiguration
    from .vault_certificate import VaultCertificate
    from .vault_secret_group import VaultSecretGroup
    from .os_profile import OSProfile
    from .network_interface_reference import NetworkInterfaceReference
    from .network_profile import NetworkProfile
    from .boot_diagnostics import BootDiagnostics
    from .diagnostics_profile import DiagnosticsProfile
    from .virtual_machine_extension_handler_instance_view import VirtualMachineExtensionHandlerInstanceView
    from .virtual_machine_agent_instance_view import VirtualMachineAgentInstanceView
    from .disk_instance_view import DiskInstanceView
    from .boot_diagnostics_instance_view import BootDiagnosticsInstanceView
    from .virtual_machine_identity import VirtualMachineIdentity
    from .virtual_machine_instance_view import VirtualMachineInstanceView
    from .virtual_machine import VirtualMachine
    from .sku import Sku
    from .upgrade_policy import UpgradePolicy
    from .virtual_machine_scale_set_identity import VirtualMachineScaleSetIdentity
    from .virtual_machine_scale_set_os_profile import VirtualMachineScaleSetOSProfile
    from .virtual_machine_scale_set_os_disk import VirtualMachineScaleSetOSDisk
    from .virtual_machine_scale_set_storage_profile import VirtualMachineScaleSetStorageProfile
    from .api_entity_reference import ApiEntityReference
    from .virtual_machine_scale_set_ip_configuration import VirtualMachineScaleSetIPConfiguration
    from .virtual_machine_scale_set_network_configuration import VirtualMachineScaleSetNetworkConfiguration
    from .virtual_machine_scale_set_network_profile import VirtualMachineScaleSetNetworkProfile
    from .virtual_machine_scale_set_extension import VirtualMachineScaleSetExtension
    from .virtual_machine_scale_set_extension_profile import VirtualMachineScaleSetExtensionProfile
    from .virtual_machine_scale_set_vm_profile import VirtualMachineScaleSetVMProfile
    from .virtual_machine_scale_set import VirtualMachineScaleSet
    from .virtual_machine_scale_set_vm_instance_ids import VirtualMachineScaleSetVMInstanceIDs
    from .virtual_machine_scale_set_vm_instance_required_ids import VirtualMachineScaleSetVMInstanceRequiredIDs
    from .virtual_machine_status_code_count import VirtualMachineStatusCodeCount
    from .virtual_machine_scale_set_instance_view_statuses_summary import VirtualMachineScaleSetInstanceViewStatusesSummary
    from .virtual_machine_scale_set_vm_extensions_summary import VirtualMachineScaleSetVMExtensionsSummary
    from .virtual_machine_scale_set_instance_view import VirtualMachineScaleSetInstanceView
    from .virtual_machine_scale_set_sku_capacity import VirtualMachineScaleSetSkuCapacity
    from .virtual_machine_scale_set_sku import VirtualMachineScaleSetSku
    from .virtual_machine_scale_set_vm import VirtualMachineScaleSetVM
    from .virtual_machine_scale_set_vm_instance_view import VirtualMachineScaleSetVMInstanceView
    from .api_error_base import ApiErrorBase
    from .inner_error import InnerError
    from .api_error import ApiError
    from .compute_long_running_operation_properties import ComputeLongRunningOperationProperties
    from .resource import Resource
    from .operation_status_response import OperationStatusResponse
from .availability_set_paged import AvailabilitySetPaged
from .virtual_machine_size_paged import VirtualMachineSizePaged
from .usage_paged import UsagePaged
from .virtual_machine_paged import VirtualMachinePaged
from .virtual_machine_scale_set_paged import VirtualMachineScaleSetPaged
from .virtual_machine_scale_set_sku_paged import VirtualMachineScaleSetSkuPaged
from .virtual_machine_scale_set_vm_paged import VirtualMachineScaleSetVMPaged
from .compute_management_client_enums import (
    StatusLevelTypes,
    OperatingSystemTypes,
    VirtualMachineSizeTypes,
    CachingTypes,
    DiskCreateOptionTypes,
    PassNames,
    ComponentNames,
    SettingNames,
    ProtocolTypes,
    ResourceIdentityType,
    UpgradeMode,
    VirtualMachineScaleSetSkuScaleType,
    InstanceViewTypes,
)

__all__ = [
    'InstanceViewStatus',
    'SubResource',
    'AvailabilitySet',
    'VirtualMachineSize',
    'VirtualMachineExtensionImage',
    'VirtualMachineImageResource',
    'VirtualMachineExtensionInstanceView',
    'VirtualMachineExtension',
    'PurchasePlan',
    'OSDiskImage',
    'DataDiskImage',
    'VirtualMachineImage',
    'UsageName',
    'Usage',
    'VirtualMachineCaptureParameters',
    'VirtualMachineCaptureResult',
    'Plan',
    'HardwareProfile',
    'ImageReference',
    'KeyVaultSecretReference',
    'KeyVaultKeyReference',
    'DiskEncryptionSettings',
    'VirtualHardDisk',
    'OSDisk',
    'DataDisk',
    'StorageProfile',
    'AdditionalUnattendContent',
    'WinRMListener',
    'WinRMConfiguration',
    'WindowsConfiguration',
    'SshPublicKey',
    'SshConfiguration',
    'LinuxConfiguration',
    'VaultCertificate',
    'VaultSecretGroup',
    'OSProfile',
    'NetworkInterfaceReference',
    'NetworkProfile',
    'BootDiagnostics',
    'DiagnosticsProfile',
    'VirtualMachineExtensionHandlerInstanceView',
    'VirtualMachineAgentInstanceView',
    'DiskInstanceView',
    'BootDiagnosticsInstanceView',
    'VirtualMachineIdentity',
    'VirtualMachineInstanceView',
    'VirtualMachine',
    'Sku',
    'UpgradePolicy',
    'VirtualMachineScaleSetIdentity',
    'VirtualMachineScaleSetOSProfile',
    'VirtualMachineScaleSetOSDisk',
    'VirtualMachineScaleSetStorageProfile',
    'ApiEntityReference',
    'VirtualMachineScaleSetIPConfiguration',
    'VirtualMachineScaleSetNetworkConfiguration',
    'VirtualMachineScaleSetNetworkProfile',
    'VirtualMachineScaleSetExtension',
    'VirtualMachineScaleSetExtensionProfile',
    'VirtualMachineScaleSetVMProfile',
    'VirtualMachineScaleSet',
    'VirtualMachineScaleSetVMInstanceIDs',
    'VirtualMachineScaleSetVMInstanceRequiredIDs',
    'VirtualMachineStatusCodeCount',
    'VirtualMachineScaleSetInstanceViewStatusesSummary',
    'VirtualMachineScaleSetVMExtensionsSummary',
    'VirtualMachineScaleSetInstanceView',
    'VirtualMachineScaleSetSkuCapacity',
    'VirtualMachineScaleSetSku',
    'VirtualMachineScaleSetVM',
    'VirtualMachineScaleSetVMInstanceView',
    'ApiErrorBase',
    'InnerError',
    'ApiError',
    'ComputeLongRunningOperationProperties',
    'Resource',
    'OperationStatusResponse',
    'AvailabilitySetPaged',
    'VirtualMachineSizePaged',
    'UsagePaged',
    'VirtualMachinePaged',
    'VirtualMachineScaleSetPaged',
    'VirtualMachineScaleSetSkuPaged',
    'VirtualMachineScaleSetVMPaged',
    'StatusLevelTypes',
    'OperatingSystemTypes',
    'VirtualMachineSizeTypes',
    'CachingTypes',
    'DiskCreateOptionTypes',
    'PassNames',
    'ComponentNames',
    'SettingNames',
    'ProtocolTypes',
    'ResourceIdentityType',
    'UpgradeMode',
    'VirtualMachineScaleSetSkuScaleType',
    'InstanceViewTypes',
]
