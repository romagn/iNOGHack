#just static dictionaries of devices containing all needed information, should be filled dynamicaly by napalm functions
device_a = {'hostname': 'router_a', 'username': 'user', 'password': 'pass123', 'network_driver': 'eos', 'optional_args'={'port': 12441}, 'neighbor_1': 'router_b', 'neighbor_2': 'router_c', 'coordinates': '53.348213, -6.275853'}
device_b = {'hostname': 'router_b', 'username': 'user', 'password': 'pass123', 'network_driver': 'ios', 'optional_args'={'port': 12442}, 'neighbor_1': 'router_a', 'neighbor_2': 'router_c', 'coordinates': '51.904760, -8.473325'}
device_c = {'hostname': 'router_c', 'username': 'user', 'password': 'pass123', 'network_driver': 'xos', 'optional_args'={'port': 12443}, 'neighbor_1': 'router_a', 'neighbor_2': 'router_b', 'coordinates': '51.495947, -0.143637'}


#list of the devices
devices_list = [device_a, device_b, device_c]

#loop which goes through each device in the given list and prints all the keys to json (not finished yet) need to figure it out
for device in devices_list:
	for key in device:
		print (json.dumps(key))
		
