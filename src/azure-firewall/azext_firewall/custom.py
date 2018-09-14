# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._client_factory import network_client_factory


# region AzureFirewall
def create_azure_firewall(cmd, resource_group_name, azure_firewall_name, location=None, tags=None):
    client = network_client_factory(cmd.cli_ctx).azure_firewalls
    AzureFirewall = cmd.get_models('AzureFirewall')
    firewall = AzureFirewall(location=location, tags=tags)
    return client.create_or_update(resource_group_name, azure_firewall_name, firewall)


def update_azure_firewall(instance, tags=None):
    if tags is not None:
        instance.tags = tags
    return instance


def list_azure_firewalls(cmd, resource_group_name=None):
    return _generic_list(cmd.cli_ctx, 'azure_firewalls', resource_group_name)

def create_af_ip_configuration(cmd, resource_group_name, azure_firewall_name, item_name,
                    public_ip_address, virtual_network_name, subnet='AzureFirewallSubnet', private_ip_address=None):
    AzureFirewallIPConfiguration, SubResource = cmd.get_models('AzureFirewallIPConfiguration', 'SubResource')
    client = network_client_factory(cmd.cli_ctx).azure_firewalls
    af = client.get(resource_group_name, azure_firewall_name)
    config = AzureFirewallIPConfiguration(
        name=item_name,
        private_ip_address=private_ip_address, 
        public_ip_address=SubResource(id=public_ip_address) if public_ip_address else None,
        subnet=SubResource(id=subnet) if subnet else None
    )
    _upsert(af, 'ip_configurations', config, 'name')
    poller = client.create_or_update(resource_group_name, azure_firewall_name, af)
    return _get_property(poller.result().ip_configurations, item_name)


def _upsert_af_rule(cmd, resource_group_name, azure_firewall_name,
                    collection_param_name, collection_name, item_key_name, item_name, params):
    pass
    # InboundNatPool = cmd.get_models('InboundNatPool')
    # ncf = network_client_factory(cmd.cli_ctx)
    # lb = ncf.load_balancers.get(resource_group_name, load_balancer_name)
    # if not frontend_ip_name:
    #     frontend_ip_name = _get_default_name(lb, 'frontend_ip_configurations', '--frontend-ip-name')
    # frontend_ip = _get_property(lb.frontend_ip_configurations, frontend_ip_name) \
    #     if frontend_ip_name else None
    # new_pool = InboundNatPool(
    #     name=item_name,
    #     protocol=protocol,
    #     frontend_ip_configuration=frontend_ip,
    #     frontend_port_range_start=frontend_port_range_start,
    #     frontend_port_range_end=frontend_port_range_end,
    #     backend_port=backend_port,
    #     enable_tcp_reset=enable_tcp_reset)
    # _upsert(lb, 'inbound_nat_pools', new_pool, 'name')
    # poller = ncf.load_balancers.create_or_update(resource_group_name, load_balancer_name, lb)
    # return _get_property(poller.result().inbound_nat_pools, item_name)


def create_af_network_rule(cmd, resource_group_name, azure_firewall_name, collection_name, item_name,
                           description=None, source_addresses=None, destination_addresses=None,
                           destination_ports=None):
    params = {
        'name': item_name,
        'description': description,
        'source_addresses': source_addresses,
        'destination_addresses': destination_addresses,
        'destination_ports': destination_ports
    }
    return _upsert_af_rule(cmd, resource_group_name, azure_firewall_name,
                           'network_rule_collections', collection_name, 'name', item_name, params)


def create_af_nat_rule(cmd, resource_group_name, azure_firewall_name, collection_name, item_name,
                       description=None, source_addresses=None, destination_addresses=None,
                       destination_ports=None, protocols=None, translated_address=None,
                       translated_port=None):
    params = {
        'name': item_name,
        'description': description,
        'source_addresses': source_addresses,
        'destination_addresses': destination_addresses,
        'destination_ports': destination_ports,
        'protocols': protocols,
        'translated_address': translated_address,
        'translated_port': translated_port
    }
    return _upsert_af_rule(cmd, resource_group_name, azure_firewall_name,
                           'nat_rule_collections', collection_name, 'name', item_name, params)


def create_af_application_rule(cmd, resource_group_name, azure_firewall_name, collection_name, item_name,
                               description=None, source_addresses=None, protocols=None, target_fqdns=None,
                               fqdn_tags=None):
    params = {
        'name': item_name,
        'description': description,
        'source_addresses': source_addresses,
        'protocols': protocols,
        'target_fqdns': target_fqdns,
        'fqdn_tags': fqdn_tags
    }
    return _upsert_af_rule(cmd, resource_group_name, azure_firewall_name,
                           'application_rule_collections', collection_name, 'name', item_name, params)
# endregion
