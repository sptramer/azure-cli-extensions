# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


# region VirtualHub
helps['network vhub'] = """
    type: group
    short-summary: Manage virtual hubs.
"""

helps['network vhub create'] = """
    type: command
    short-summary: Create a virtual hub.
"""

helps['network vhub list'] = """
    type: command
    short-summary: List virtual hubs.
"""

helps['network vhub show'] = """
    type: command
    short-summary: Get the details of a virtual hub.
"""

helps['network vhub update'] = """
    type: command
    short-summary: Update settings of a virtual hub.
"""

helps['network vhub delete'] = """
    type: command
    short-summary: Delete a virtual hub.
"""
# endregion

# region VirtualWAN
helps['network vwan'] = """
    type: group
    short-summary: Manage virtual WANs.
"""

helps['network vwan create'] = """
    type: command
    short-summary: Create a virtual WAN.
"""

helps['network vwan list'] = """
    type: command
    short-summary: List virtual WANs.
"""

helps['network vwan show'] = """
    type: command
    short-summary: Get the details of a virtual WAN.
"""

helps['network vwan update'] = """
    type: command
    short-summary: Update settings of a virtual WAN.
"""

helps['network vwan delete'] = """
    type: command
    short-summary: Delete a virtual WAN.
"""
# endregion
