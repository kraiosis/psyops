import sys
def check_installed_software():
    try:
        if(sys.platform == "win32"):
            import winreg
            path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, subkey_name) as subkey:
                            print(winreg.QueryValueEx(subkey, "DisplayName")[0])
                    except EnvironmentError:
                        continue
        elif(sys.platform == "linux"):
            import apt
            cache = apt.Cache()
            for pkg in cache:
                if pkg.is_installed:
                    print(pkg.name)
    except KeyboardInterrupt:
        print("\nExiting Program.")
        sys.exit()