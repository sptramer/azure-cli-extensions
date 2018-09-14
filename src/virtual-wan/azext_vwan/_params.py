# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from knack.arguments import CLIArgumentType

from azure.cli.core.commands.parameters import (
    get_resource_name_completion_list, tags_type)
from azure.cli.core.commands.validators import get_default_location_from_resource_group


# pylint: disable=too-many-locals, too-many-branches, too-many-statements
def load_arguments(self, _):

    # region VirutalWAN
    vwan_name_type = CLIArgumentType(options_list=('--vwan-name',), metavar='NAME', help='Name of the virtual WAN.', id_part='name', completer=get_resource_name_completion_list('Microsoft.Network/virtualWANs'))
    vhub_name_type = CLIArgumentType(options_list=('--vhub-name',), metavar='NAME', help='Name of the virtual hub.', id_part='name', completer=get_resource_name_completion_list('Microsoft.Network/networkHubs'))

    with self.argument_context('network vwan') as c:
        c.argument('virtual_wan_name', vwan_name_type, options_list=['--name', '-n'])
        c.argument('location', get_location_type(self.cli_ctx), validator=get_default_location_from_resource_group)
        c.argument('branch_to_branch_traffic', arg_type=get_three_state_flag(), help='Allow branch-to-branch traffic flow.')
        c.argument('vnet_to_vnet_traffic', arg_type=get_three_state_flag(), help='Allow VNet-to-VNet traffic flow.')
        c.argument('security_provider_name', help='The security provider name.')
        c.argument('office365_category', help='The office local breakout category.')
        c.argument('disable_vpn_encryption', arg_type=get_three_state_flag(), help='State of VPN encryption.')

    with self.argument_context('network vhub') as c:
        c.argument('virtual_hub_name', vhub_name_type, options_list=['--name', '-n'])
        c.argument('location', get_location_type(self.cli_ctx), validator=get_default_location_from_resource_group)
    # enregion
