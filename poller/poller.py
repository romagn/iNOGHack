import napalm
import argparse
import time


def parse_args():
    p = argparse.ArgumentParser('simple poller')
    p.add_argument('-d', '--device', help='device to poll')
    p.add_argument('-o', '--os', help='os of the device')
    return p.parse_args()


def main():
    # load hosts from inventory (required for credentials)
    with open('../data/inventory.json') as f:
      inventory = json.load(f)
   
    # load neighbors (required for polling)
    with open('../data/neighbors.json') as f:
      neighbors = json.load(f)

    if_data = {}

    for device in neighbors:
        username=inventory[device][]
        password=device['password'], network_driver=device['network_driver'], optional_args=device['optional_args'])

    with driver(hostname=args.device, password='123', username='root') as d:
        for interface, data in dev.get_interfaces().iter():
            if_data[interface] = int(data['is_up'])
    with open('/var/tmp/data/{}.json'.format(args.device), 'w') as f:
        f.write(json.dumps(if_data))

if __name__ == '__main__':
    main()
