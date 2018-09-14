# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

# region AzureFirewalls
helps['network firewall'] = """
    type: group
    short-summary: Manage and configure Azure Firewalls.
"""

helps['network firewall create'] = """
    type: command
    short-summary: Create an Azure Firewall.
"""

helps['network firewall delete'] = """
    type: command
    short-summary: Delete an Azure Firewall.
"""

helps['network firewall list'] = """
    type: command
    short-summary: List Azure Firewalls.
"""

helps['network firewall show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall.
"""

helps['network firewall update'] = """
    type: command
    short-summary: Update an Azure Firewall.
"""
# endregion

# region AzureFirewall IP Configurations
helps['network firewall ip-config'] = """
    type: group
    short-summary: Manage and configure Azure Firewall IP configurations.
"""

helps['network firewall ip-config create'] = """
    type: command
    short-summary: Create an Azure Firewall IP configuration.
"""

helps['network firewall ip-config delete'] = """
    type: command
    short-summary: Delete an Azure Firewall IP configuration.
"""

helps['network firewall ip-config list'] = """
    type: command
    short-summary: List Azure Firewall IP configurations.
"""

helps['network firewall ip-config show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall IP configuration.
"""

helps['network firewall ip-config update'] = """
    type: command
    short-summary: Update an Azure Firewall IP configuration.
"""
# endregion

# region AzureFirewall Network Rules
helps['network firewall network-rule'] = """
    type: group
    short-summary: Manage and configure Azure Firewall network rules.
"""

helps['network firewall network-rule create'] = """
    type: command
    short-summary: Create an Azure Firewall network rule.
"""

helps['network firewall network-rule delete'] = """
    type: command
    short-summary: Delete an Azure Firewall network rule.
"""

helps['network firewall network-rule list'] = """
    type: command
    short-summary: List Azure Firewall network rules.
"""

helps['network firewall network-rule show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall network rule.
"""

helps['network firewall network-rule update'] = """
    type: command
    short-summary: Update an Azure Firewall network rule.
"""
# endregion

# region AzureFirewall NAT Rules
helps['network firewall nat-rule'] = """
    type: group
    short-summary: Manage and configure Azure Firewall NAT rules.
"""

helps['network firewall nat-rule create'] = """
    type: command
    short-summary: Create an Azure Firewall NAT rule.
"""

helps['network firewall nat-rule delete'] = """
    type: command
    short-summary: Delete an Azure Firewall NAT rule.
"""

helps['network firewall nat-rule list'] = """
    type: command
    short-summary: List Azure Firewall NAT rules.
"""

helps['network firewall nat-rule show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall NAT rule.
"""

helps['network firewall nat-rule update'] = """
    type: command
    short-summary: Update an Azure Firewall NAT rule.
"""
# endregion

# region AzureFirewall Application Rules
helps['network firewall application-rule'] = """
    type: group
    short-summary: Manage and configure Azure Firewall application rules.
"""

helps['network firewall application-rule create'] = """
    type: command
    short-summary: Create an Azure Firewall application rule.
"""

helps['network firewall application-rule delete'] = """
    type: command
    short-summary: Delete an Azure Firewall application rule.
"""

helps['network firewall application-rule list'] = """
    type: command
    short-summary: List Azure Firewall application rules.
"""

helps['network firewall application-rule show'] = """
    type: command
    short-summary: Get the details of an Azure Firewall application rule.
"""

helps['network firewall application-rule update'] = """
    type: command
    short-summary: Update an Azure Firewall application rule.
"""
# endregion
