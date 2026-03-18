import psutil
import time
import os
import sys
import platform

def monitor_resources():
    """
    Monitor system resources
    """
    print("Monitoring System Resources:")
    # while True:
    # --- CPU Usage ---
    # interval=1 samples CPU usage over 1 second for a meaningful percentage
    cpu_percent = psutil.cpu_percent(interval=1) 
    cpu_count_logical = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    
    # --- RAM Usage ---
    # psutil.virtual_memory() returns a named tuple with memory details
    mem_info = psutil.virtual_memory()
    
    # --- Network Usage ---
    # psutil.net_io_counters() returns a named tuple with network I/O statistics
    net_io = psutil.net_io_counters()

    print("-" * 40)
    print(f"Operating System: {platform.system()} - {os.name} / {sys.platform}")
    print(f"Total CPU Usage: {cpu_percent}%")
    print(f"Logical CPU Count: {cpu_count_logical}")
    if cpu_freq:
        print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")
    
    print(f"Total RAM: {mem_info.total / (1024**3):.2f} GB")
    print(f"Used RAM: {mem_info.used / (1024**3):.2f} GB")
    print(f"RAM Usage Percentage: {mem_info.percent}%")

    print(f"Network Sent (bytes): {net_io.bytes_sent}")
    print(f"Network Received (bytes): {net_io.bytes_recv}")

    disk_partitions = psutil.disk_partitions()
    for partition in disk_partitions:
        print(f'Disk Partition: {partition.device} - {partition.mountpoint} - {partition.fstype} - {partition.opts}') # (partition)
        # Get disk usage statistics
        usage = psutil.disk_usage(partition.mountpoint)

        # Convert bytes to gigabytes for better readability
        total_gb = usage.total / (1024**3)
        used_gb = usage.used / (1024**3)
        free_gb = usage.free / (1024**3)
        percent_used = usage.percent

        print(f"--- Disk Usage for {partition.mountpoint} ---")
        print(f"Total: {total_gb:.2f} GB")
        print(f"Used: {used_gb:.2f} GB")
        print(f"Free: {free_gb:.2f} GB")
        print(f"Usage Percentage: {percent_used}%")
        print("-" * 30)
        
if __name__ == "__main__":
    try:
        monitor_resources()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

