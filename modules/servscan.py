import socket
import sys
import concurrent.futures
from datetime import datetime

# Define the target
def portscan(hostname):
    """
    Scan for open ports on a target device.
    """
    if len(hostname) > 0:
        target = socket.gethostbyname('localhost') # Translate hostname to IPv4
    else:
        print("Invalid amount of arguments. Please provide a target hostname or IP address.")
        # sys.exit()

    # Print a banner
    print("-" * 45)
    print("Scan Target: " + target)
    print("Scanning started: " + str(datetime.now()))
    print("-" * 45)

    # Scan ports
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Set a timeout of 1 second

        # Use a multithreaded approach to scan ports
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(scan_port, target, port) for port in range(1, 1024)]
            for future in concurrent.futures.as_completed(futures):
                port, result = future.result()
                if result == 0:
                    print(f"[+] TCP Port {port} is open")

        s.close()

    except KeyboardInterrupt:
        print("\nExiting Program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Server not responding.")
        sys.exit()

    print("-" * 45)
    print("Scanning completed: " + str(datetime.now()))
    print("-" * 45)

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port)) # Returns 0 if port is open
    s.close()
    return port, result
