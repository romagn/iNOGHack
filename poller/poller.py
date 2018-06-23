import napalm
import argparse
import time


def main():
    args = parse_args()
    driver = napalm.get_network_driver(args.os)
    if_data = {}
    with driver(hostname=args.device, password='123', username='root') as d:
        for interface, data in dev.get_interfaces().iter():
            if_data[interface] = int(data['is_up'])
    with open('/var/tmp/data/{}.json'.format(args.device), 'w') as f:
        f.write(json.dumps(if_data))

if __name__ == '__main__':
    main()
