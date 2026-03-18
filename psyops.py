# File: psyops.py   
# Author: Federico Guzman    
# Description: Basic tools for server and terminal admin/ops.
# Date: 2026-03-17
# Revision: 1
# Requires:psutil library | run: pip install psutil

from modules.servscan import portscan  
from modules.processchk import proscan
from modules.stats import monitor_resources
from modules.users import get_current_users
from modules.memgame import memgame

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
        print("5. Memory Game")
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
            print("\n>> Memgame...")
            # Add code here for memgame
            memgame()
        elif choice == 'q':
            print("\n>> Exiting application. Goodbye!")
            break  # Exit the while loop
        else:
            print("\n>> Invalid input. Please select a valid option (1, 2, 3, or Q).")

# Run the application
if __name__ == "__main__":
    menu_driven_app()
