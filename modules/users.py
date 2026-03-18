import psutil

def get_current_users():
    """
    Get the name of the currently logged-in user
    """
    # Get a list of all currently logged-in users
    users = psutil.users()
    current_user_name = next((user.name for user in users), None)
    if current_user_name:
        print(f"Current user: {current_user_name}")
    else:
        print("No active users found.")

    # You can also iterate through all users
    print("All logged-in users:")
    for user in users:
        print(f"- {user.name} (Host: {user.host}, Terminal: {user.terminal}")
