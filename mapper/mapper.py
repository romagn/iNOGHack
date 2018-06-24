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

    neighbors = []

    for interface in lldp_neighbors.iteritems():
        for neighbor in interface[1]:
           #                 localIf, nbrHostname, nbrIf
           # neighbors.append([interface[0],neighbor['hostname'], neighbor['port']])
           neighbors.append({'localIf': interface[0], 'nbrHostname': neighbor['hostname'], 'nbrIf': neighbor['port']})
           
    devices[hostname] = []
    devices[hostname].append({
       'snmp_location': snmp_information['location'],
       'lldp_neighbors': neighbors
    }) 

    # close the session with the device.
    device.close()
    print('Done.')

if __name__ == '__main__':
    # load hosts from inventory
    with open('inventory.json') as f:
      inventory = json.load(f)

    devices = {}
    
    #loop which goes through each device in the inventory and dumps all neighbor information to json
    for device in inventory:
        main(hostname=device['hostname'], username=device['username'], password=device['password'], network_driver=device['network_driver'], optional_args=device['optional_args'])

    with open('/var/tmp/neighbors.json', 'w') as f:
        f.write(json.dumps(devices, indent=4, sort_keys=True))
