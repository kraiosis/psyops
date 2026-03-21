# File: psyops.py   
# Author: Federico Guzman    
# Description: Basic tools for server and terminal admin/ops.
# Date: 2026-03-17
# Revision: 1
# Requires:psutil library | run: pip install psutil

# check if psutil is installed
import sys
import importlib.util
spec = importlib.util.find_spec("psutil")
if spec is None:
    if(sys.platform == "win32"):
        print("psutil is not installed. Please install it using 'pip install psutil'")
        exit()
    else:
        print("psutil is not installed. Please install it using 'sudo apt install python3-psutil'")
        exit()


from modules.servscan import portscan  
from modules.processchk import proscan
from modules.stats import monitor_resources
from modules.users import get_current_users
from modules.software import check_installed_software
from modules.memgame import memgame
from modules.netscan import netscan

def menu_driven_app():
    """
    Basic tools for server and terminal admin/ops.
    """
    while True:
        print("\n*** Basic tools for server and terminal admin/ops with python ***")
        print("*** Application Menu ***\n")
        print("1. Port Scanning")
        print("2. Process Scanning")
        print("3. Check performance")
        print("4. Get logged in users")
        print("5. Check installed software")
        print("6. Network Scanning")
        print("7. Memory Game")
        print("Q. Quit the application")

        # Get user input and convert to lowercase for easier handling
        choice = input("Enter your choice: ").lower()

        # Use Unicode for symbols
        # print("✅ Success!")
        # print("❌ Error!")
        # print("⚙️ Processing...")
        # print("⌛ Working...")
        # print("🚀 Launching...")

        if choice == '1':
            print("\n>> Port Scanning...")
            print("Disclaimer: This will scan all ports on the target. \nScanning can take some time depending on the target. \nScanning is not recommended for large networks. \nScanning networks without permissions is iligal")
            host = input("Enter the host IP address: ")            
            portscan(host)
        elif choice == '2':
            print("\n>> Process Scanning...")           
            proscan()
        elif choice == '3':
            print("\n>> Checking performance...")
            # Add code here for checking performance
            monitor_resources()
        elif choice == '4':
            print("\n>> Getting logged in users...")
            # Add code here for getting logged in users
            get_current_users()
        elif choice == '5':
            print("\n>> Getting installed software...")
            check_installed_software()
        elif choice == '6':
            print("\n>> Netscanning...")
            # Add code here for netscanning
            netvalue = input("IP/Mask address (192.168.1.0/24): ")            
            netscan(netvalue)
        elif choice == '7':
            print("\n>> Memgame...")
            # Add code here for memgame
            memgame()
        elif choice == 'q':
            print("\n>> Exiting application. Goodbye!")
            break  # Exit the while loop
        else:
            print("\n>> Invalid input. Please select a valid option (1, 2, 3, 4, 5, 6 or Q).")

# Run the application
if __name__ == "__main__":
    menu_driven_app()
