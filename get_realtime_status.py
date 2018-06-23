# Sample script to demonstrate loading a config for a device.
#
# Note: this script is as simple as possible: it assumes that you have
# followed the lab setup in the quickstart tutorial, and so hardcodes
# the device IP and password.  You should also have the
# 'new_good.conf' configuration saved to disk.
from __future__ import print_function

import napalm
import sys
import os
import json

def main(hostname, username, password, network_driver, optional_args):
    """Load a config for the device."""

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

    print(json.dumps(facts))
    print(json.dumps(snmp_information))
    print(json.dumps(lldp_neighbors))

    # close the session with the device.
    device.close()
    print('Done.')

if __name__ == '__main__':
#    if len(sys.argv) < 2:
#        print('Please supply the full path to "new_good.conf"')
#        sys.exit(1)
#    config_file = sys.argv[1]
#    main(config_file)
    main(hostname='127.0.0.1', username='vagrant', password='vagrant', network_driver='eos', optional_args={'port': 12443})
