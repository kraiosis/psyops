import psutil

def proscan():
    """
    Scan and list all running processes
    """
    try:
        pnum=runum=slnum=stnum=0
        print("Listing all running processes:")
        for proc in psutil.process_iter(['pid', 'name', 'status']):   
            pnum += 1
            try:
                # Access process information using the Process instance methods
                print(f"PID: {proc.pid}, Name: {proc.name()}, Status: {proc.status()}")
                if proc.status() == psutil.STATUS_RUNNING:
                    runum += 1
                elif proc.status() == psutil.STATUS_SLEEPING:
                    slnum += 1
                elif proc.status() == psutil.STATUS_STOPPED:
                    stnum += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle cases where the process is no longer available or access is denied
                pass
        print(f"Total number of processes: {pnum} Running: {runum} Sleeping: {slnum} Stopped: {stnum}")

    except Exception as e:
        print(f"An error occurred: {e}")
