# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
from knack.util import CLIError
from azure.cli.core.util import sdk_no_wait

from ._client_factory import network_client_factory


def build_af_rule_collection_create(collection_param_name):
    
    def create_af_rule_collection(cmd, resource_group_name, azure_firewall_name, collection_name,
                                  priority, action=None):
        from azure.cli.command_modules.network.custom import _upsert
        client = network_client_factory(cmd.cli_ctx).azure_firewalls
        af = client.get(resource_group_name, azure_firewall_name)
        params = {
            'name': collection_name,
            'priority': priority,
            'action': {'type': action}
        }
        _upsert(af, collection_param_name, params, 'name')
        poller = client.create_or_update(resource_group_name, azure_firewall_name, af)
        return _get_property(getattr(poller.result(), collection_param_name), item_name)

    func_name = 'create_af_{}'.format(collection_param_name)
    setattr(sys.modules[__name__], func_name, create_af_rule_collection)
    return func_name

def _get_property(items, name):
    result = next((x for x in items if x.name.lower() == name.lower()), None)
    if not result:
        raise CLIError("Property '{}' does not exist".format(name))
    else:
        return result


def _set_param(item, prop, value):
    if value == '':
        setattr(item, prop, None)
    elif value is not None:
        setattr(item, prop, value)


def list_network_resource_property(resource, prop):
    """ Factory method for creating list functions. """

    def list_func(cmd, resource_group_name, resource_name):
        client = getattr(network_client_factory(cmd.cli_ctx), resource)
        return client.get(resource_group_name, resource_name).__getattribute__(prop)

    func_name = 'list_network_resource_property_{}_{}'.format(resource, prop)
    setattr(sys.modules[__name__], func_name, list_func)
    return func_name


def get_network_resource_property_entry(resource, prop):
    """ Factory method for creating get functions. """

    def get_func(cmd, resource_group_name, resource_name, item_name):
        client = getattr(network_client_factory(cmd.cli_ctx), resource)
        items = getattr(client.get(resource_group_name, resource_name), prop)

        result = next((x for x in items if x.name.lower() == item_name.lower()), None)
        if not result:
            raise CLIError("Item '{}' does not exist on {} '{}'".format(
                item_name, resource, resource_name))
        else:
            return result

    func_name = 'get_network_resource_property_entry_{}_{}'.format(resource, prop)
    setattr(sys.modules[__name__], func_name, get_func)
    return func_name


def delete_network_resource_property_entry(resource, prop):
    """ Factory method for creating delete functions. """

    def delete_func(cmd, resource_group_name, resource_name, item_name, no_wait=False):  # pylint: disable=unused-argument
        client = getattr(network_client_factory(cmd.cli_ctx), resource)
        item = client.get(resource_group_name, resource_name)
        keep_items = \
            [x for x in item.__getattribute__(prop) if x.name.lower() != item_name.lower()]
        _set_param(item, prop, keep_items)
        if no_wait:
            sdk_no_wait(no_wait, client.create_or_update, resource_group_name, resource_name, item)
        else:
            result = sdk_no_wait(no_wait, client.create_or_update, resource_group_name, resource_name, item).result()
            if next((x for x in getattr(result, prop) if x.name.lower() == item_name.lower()), None):
                raise CLIError("Failed to delete '{}' on '{}'".format(item_name, resource_name))

    func_name = 'delete_network_resource_property_entry_{}_{}'.format(resource, prop)
    setattr(sys.modules[__name__], func_name, delete_func)
    return func_name
