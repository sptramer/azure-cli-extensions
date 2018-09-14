# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType

from ._client_factory import cf_virtual_wans, cf_virtual_hubs


# pylint: disable=too-many-locals, too-many-statements
def load_command_table(self, _):

    network_vhub_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.network.operations.virtual_hubs_operations#VirtualHubsOperations.{}',
        client_factory=cf_virtual_hubs,
        min_api='2018-08-01'
    )

    network_vwan_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.network.operations.virtual_wans_operations#VirtualWansOperations.{}',
        client_factory=cf_virtual_wans,
        min_api='2018-08-01'
    )

    # region VirtualWANs
    with self.command_group('network vwan', network_vwan_sdk) as g:
        g.custom_command('create', 'create_virtual_wan')
        g.show_command('show')

    with self.command_group('network vhub', network_vhub_sdk) as g:
        g.custom_command('create', 'create_virtual_hub')
        g.show_command('show')
    # endregion
