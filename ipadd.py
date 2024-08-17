import ipaddress
def ip_to_bin(ip):
    return ''.join([format(int(octet), '08b') for octet in ip.split('.')])

def bin_to_ip(bin_str):
    return '.'.join([str(int(bin_str[i:i+8], 2)) for i in range(0, 32, 8)])

def calculate_network_address(ip, subnet):
    ip_bin = ip_to_bin(ip)
    subnet_bin = ip_to_bin(subnet)
    network_bin = ''.join([str(int(ip_bin[i]) & int(subnet_bin[i])) for i in range(32)])
    return bin_to_ip(network_bin)

def calculate_broadcast_address(ip, subnet):
    ip_bin = ip_to_bin(ip)
    subnet_bin = ip_to_bin(subnet)
    network_bin = ''.join([str(int(ip_bin[i]) & int(subnet_bin[i])) for i in range(32)])
    broadcast_bin = network_bin[:subnet_bin.count('1')] + '1' * subnet_bin.count('0')
    return bin_to_ip(broadcast_bin)

def calculate_netmask(prefixlen):
    return bin_to_ip('1' * prefixlen + '0' * (32 - prefixlen))

def calculate_prefixlen(subnet):
    return ip_to_bin(subnet).count('1')

def calculate_first_last_usable(network_address, broadcast_address):
    first_usable = bin_to_ip(format(int(ip_to_bin(network_address), 2) + 1, '032b'))
    last_usable = bin_to_ip(format(int(ip_to_bin(broadcast_address), 2) - 1, '032b'))
    return first_usable, last_usable

def calculate_usable_hosts(prefixlen):
    return (2**(32 - prefixlen)) - 2 if prefixlen < 31 else 0

def calculate_wildcard(subnet):
    subnet_bin = ip_to_bin(subnet)
    wildcard_bin = ''.join(['1' if bit == '0' else '0' for bit in subnet_bin])
    return bin_to_ip(wildcard_bin)

def calc_net_details(ip, subnet):
    if '.' in subnet:
        prefixlen = calculate_prefixlen(subnet)
    else:
        prefixlen = int(subnet)
        subnet = calculate_netmask(prefixlen)
    
    network_address = calculate_network_address(ip, subnet)
    broadcast_address = calculate_broadcast_address(ip, subnet)
    first_usable, last_usable = calculate_first_last_usable(network_address, broadcast_address)
    usable_hosts = calculate_usable_hosts(prefixlen)
    wildcard = calculate_wildcard(subnet)
    
    print(f"Address:               {ip}")
    print(f"Network Address:       {network_address}")
    print(f"Broadcast:             {broadcast_address}")
    print(f"Netmask:               {subnet}")
    print(f"Slash:                 /{prefixlen}")
    print(f"First Usable Host:     {first_usable}")
    print(f"Last Usable Host:      {last_usable}")
    print(f"Usable Hosts:          {usable_hosts}")
    print(f"Wildcard:              {wildcard}")

def check(Ip): 
    try:
        ipaddress.ip_address(Ip)
        return Ip
        
    except ValueError:
        
        print("Invalid IP address")

def main():
    ip = input("Enter the IP address: ")
    check(ip)
    
    subnet = input("Enter the subnet mask or prefix (e.g., 255.255.255.0 or 24): ")
    calc_net_details(ip, subnet)

if __name__=="__main__":
    main()
