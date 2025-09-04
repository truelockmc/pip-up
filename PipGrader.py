#!/usr/bin/python3

import subprocess
import sys
import time

def get_outdated_packages():
    """Getting List of outdated packages..."""
    try:
        result = subprocess.check_output([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=columns'])
        return result.decode().splitlines()[2:]  # Die ersten zwei Zeilen sind Kopfzeilen, die wir ignorieren
    except subprocess.CalledProcessError as e:
        print(f"Error while fetching outdated packages: {e}")
        sys.exit(1)

def update_package(package_name):
    """Updates a single package."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', package_name])
        print(f"Successfully updated: {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error while updating {package_name}: {e}")

def update_pip():
    """Ensures pip is updated."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        print("Successfully updated: pip")
    except subprocess.CalledProcessError as e:
        print(f"Error while updating pip: {e}")

def main():
    
    # Update pip
    print("Updating pip...")
    update_pip()
    
    print("Getting list of outdated packages...")
    outdated_packages = get_outdated_packages()

    if not outdated_packages:
        print("All packages are up to date.")
    else:
        print("Updating packages...")
        for package in outdated_packages:
            package_name = package.split()[0]  # The package name is in the first column
            update_package(package_name)

    # Final notification
    print("\nAll packages, including pip, have been successfully updated.")
    
    # Optional: Wait for a few seconds before closing
    time.sleep(30)

if __name__ == "__main__":
    main()

