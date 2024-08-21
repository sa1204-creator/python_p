read this file before using the script

this python script provides you with a detailed informations about your VLSM subnets
it asks you first to type an IP address along with its prefix and number of subnets you want to create
than it gives you the : 
Network Address, Broadcast, Netmask,
Slash, First Usable Host, Last Usable Host,
Usable Hosts Wildcard .

example : 

INPUTE : 

IP address: 192.168.1.0
Initial prefix: 24
Number of subnets: 3
Hosts per subnet: 50, 30, 20

OUTPUTE : 

VLSM Subnetting:
Subnet 1:
  Network Address: 192.168.1.0/26
  Subnet Mask:     255.255.255.192
  First IP:        192.168.1.1
  Last IP:         192.168.1.62
  Broadcast:       192.168.1.63
  Usable Hosts:    62
Subnet 2:
  Network Address: 192.168.1.64/27
  Subnet Mask:     255.255.255.224
  First IP:        192.168.1.65
  Last IP:         192.168.1.94
  Broadcast:       192.168.1.95
  Usable Hosts:    30
Subnet 3:
  Network Address: 192.168.1.96/27
  Subnet Mask:     255.255.255.224
  First IP:        192.168.1.97
  Last IP:         192.168.1.126
  Broadcast:       192.168.1.127
  Usable Hosts:    30


the script follows the clean code practices 
it has  12 function 

- the following two functions to convert IP from binary and from binary to IP 
ip_to_bin(ip)
bin_to_ip(bin_str)

- the followin seven functions to calculate the Network Address, Broadcast, Netmask, Slash, First Usable Host, Last Usable Host, Usable Hosts Wildcard .
calculate_network_address(ip, subnet)
calculate_broadcast_address(ip, subnet)
calculate_netmask(prefixlen)
calculate_prefixlen(subnet)
calculate_first_last_usable(network_address, broadcast_address)
calculate_usable_hosts(prefixlen)
calculate_wildcard(subnet)

- the following function prints the informations that were calculated previously 
calc_net_details(ip, subnet)

- the following function does calculate the VLSM subnets and prints thiers detaild informations using the previous functions 
vlsm_subnetting(network_ip, prefix, hosts)

- and lastly the main function start the excution of the code 
main()

thanks for reading this