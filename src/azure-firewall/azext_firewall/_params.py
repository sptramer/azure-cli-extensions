# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from knack.arguments import CLIArgumentType

from azure.cli.core.commands.parameters import (
    get_resource_name_completion_list, tags_type)
from azure.cli.core.commands.validators import get_default_location_from_resource_group

from ._validators import validate_vnet_tap


# pylint: disable=too-many-locals, too-many-branches, too-many-statements
def load_arguments(self, _):

    firewall_name_type = CLIArgumentType(options_list='--firewall-name', metavar='NAME', help='Azure Firewall name.', id_part='name', completer=get_resource_name_completion_list('Microsoft.Network/azureFirewalls'))

    # region AzureFirewalls
    af_subresources = [
        {'name': 'ip-config', 'display': 'IP configuration', 'ref': 'ip_configurations'},
        {'name': 'network-rule collection', 'display': 'network rule collection', 'ref': 'network_rule_collections'},
        {'name': 'nat-rule collection', 'display': 'NAT rule colleciton', 'ref': 'nat_rule_collections'},
        {'name': 'application-rule collection', 'display': 'application rule collection', 'ref': 'application_rule_collections'},
    ]
    for item in af_subresources:
        with self.argument_context('network firewall {}'.format(item['name'])) as c:
            c.argument('collection_name', options_list=('--name', '-n'), help='The name of the {}'.format(item['display']), completer=get_lb_subresource_completion_list(item['ref']), id_part='child_name_1')
            c.argument('resource_name', options_list=('--firewall-name',), help='The name of the Azure firewall.', completer=get_resource_name_completion_list('Microsoft.Network/azureFirewalls'))
            c.argument('azure_firewall_name', firewall_name_type)

    for scope in ['network-rule', 'application-rule']:
        with self.argument_context('network firewall {} collection'.format(scope)) as c:
            c.argument('action', arg_type=get_enum_type(['Allow', 'Deny']))

    with self.argument_context('network firewall nat-rule collection') as c:
        c.argument('action', arg_type=get_enum_type(['Snat', 'Dnat']))

    af_sub_subresources = [
        {'name': 'network-rule', 'display': 'network rule', 'ref': 'network_rule_collections'},
        {'name': 'nat-rule', 'display': 'NAT rule', 'ref': 'nat_rule_collections'},
        {'name': 'application-rule', 'display': 'application rule', 'ref': 'application_rule_collections'},
    ]
    for item in af_sub_subresources:
        with self.argument_context('network firewall {}'.format(item['name'])) as c:
            c.argument('item_name', options_list=('--name', '-n'), help='The name of the {}'.format(item['display']), completer=get_lb_subresource_completion_list(item['ref']), id_part='child_name_1')
            c.argument('resource_name', options_list=('--firewall-name',), help='The name of the Azure firewall.', completer=get_resource_name_completion_list('Microsoft.Network/azureFirewalls'))
            c.argument('azure_firewall_name', firewall_name_type)

    with self.argument_context('network firewall') as c:
        c.argument('azure_firewall_name', firewall_name_type, options_list=['--name', '-n'])
        c.argument('location', get_location_type(self.cli_ctx), validator=get_default_location_from_resource_group)
        c.argument('priority', type=int, help='Priority value from 100 (high) to 65000 (low).')

    with self.argument_context('network firewall ip-config') as c:
        c.argument('subnet', validator=get_subnet_validator(), help='Name or ID of an existing subnet. If name is specified, also specify --vnet-name.')
        c.argument('public_ip_address', help='Name or ID of the public IP to use.', validator=get_public_ip_validator())
    # endregion
