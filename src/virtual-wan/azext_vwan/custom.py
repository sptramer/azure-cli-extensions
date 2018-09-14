# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._client_factory import network_client_factory


# region VirtualWAN
def create_virtual_wan(cmd, resource_group_name, virtual_wan_name, tags=None, location=None,
                       security_provider_name=None, branch_to_branch_traffic=None,
                       vnet_to_vnet_traffic=None, office365_category=None, disable_vpn_encryption=None):
    client = network_client_factory(cmd.cli_ctx).virtual_wans
    VirtualWAN = cmd.get_models('VirtualWAN')
    wan = VirtualWAN(
        tags=tags,
        location=location,
        disable_vpn_encryption=disable_vpn_encryption,
        security_provider_name=security_provider_name,
        allow_branch_to_branch_traffic=branch_to_branch_traffic,
        allow_vnet_to_vnet_traffic=vnet_to_vnet_traffic,
        office365_local_breakout_category=office365_category
    )
    return client.create_or_update(resource_group_name, virtual_wan_name, wan)


def create_virtual_hub(cmd, resource_group_name, virtual_hub_name, address_prefix, virtual_wan,
                       location=None, tags=None):
    client = network_client_factory(cmd.cli_ctx).virtual_hubs
    VirtualHub, SubResource = cmd.get_models('VirtualHub', 'SubResource')
    hub = VirtualHub(
        tags=tags,
        location=location,
        address_prefix=address_prefix,
        virtual_wan=SubResource(id=virtual_wan)
    )
    return client.create_or_update(resource_group_name, virtual_hub_name, hub)
# endregion
