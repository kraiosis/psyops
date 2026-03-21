import networkscan

# Main function
def netscan(netvalue):
    """
    Scan for connected devices on a network.
    """
    if len(netvalue) > 0:
        target = netvalue # Translate hostname to IPv4
    else:
        # print("Invalid amount of arguments. Please provide a target hostname or IP address.")
        target = "192.168.1.0/24"
        
    # Define the network to scan
    my_network = target

    # Create the object
    my_scan = networkscan.Networkscan(my_network)

    # Display information
    print("Network to scan: " + str(my_scan.network))
    print("Prefix to scan: " + str(my_scan.network.prefixlen))
    print("Number of hosts to scan: " + str(my_scan.nbr_host))

    # Run the network scan
    print("Scanning hosts...")

    # Run the scan of hosts using pings
    my_scan.run()

    # Display information
    print("List of hosts found:")

    # Display the IP address of all the hosts found
    for i in my_scan.list_of_hosts_found:
        print(i)

    # Display information
    print("Number of hosts found: " + str(my_scan.nbr_host_found))