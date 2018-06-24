from __future__ import print_function

import napalm
import sys
import os
import json

def main(hostname, username, password, network_driver, optional_args):
    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver(network_driver)

    # Connect:
    device = driver(hostname=hostname, username=password,
                    password=password, optional_args=optional_args)


    print('Opening ...')
    device.open()

    print('Get facts ...')
    facts = device.get_facts()

    print('Get SNMP information ...')
    snmp_information = device.get_snmp_information()

    print('Get LLDP neighbors ...')
    lldp_neighbors = device.get_lldp_neighbors()

    neighbors[hostname] = []
    neighbors[hostname].append({
       'snmp_location': snmp_information['location'],
       'lldp_neighbors': lldp_neighbors
    }) 

    # close the session with the device.
    device.close()
    print('Done.')

if __name__ == '__main__':
    #just static dictionaries of devices containing all needed information, should be filled dynamicaly by napalm functions
    inventory_a = {'hostname': '127.0.0.1', 'username': 'vagrant', 'password': 'vagrant', 'network_driver': 'eos', 'optional_args': {'port': 12443}}
    inventory_b = {'hostname': '127.0.0.2', 'username': 'vagrant', 'password': 'vagrant', 'network_driver': 'eos', 'optional_args': {'port': 22443}}
    
    #list of the devices
    inventory = [inventory_a, inventory_b]

    neighbors = {}
    
    #loop which goes through each device in the given list and prints all the keys to json (not finished yet) need to figure it out
    for device in inventory:
        main(hostname=device['hostname'], username=device['username'], password=device['password'], network_driver=device['network_driver'], optional_args=device['optional_args'])

    with open('/var/tmp/neighbors.json', 'w') as f:
        f.write(json.dumps(neighbors, indent=4, sort_keys=True))
