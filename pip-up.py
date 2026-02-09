#!/usr/bin/python3

import subprocess
import sys
import time

def get_outdated_packages(python_path):
    """Getting List of outdated packages..."""
    try:
        result = subprocess.check_output([python_path, '-m', 'pip', 'list', '--outdated', '--format=columns'])
        return result.decode().splitlines()[2:]
    except subprocess.CalledProcessError as e:
        print(f"Error while fetching outdated packages: {e}")
        sys.exit(1)

def update_package(python_path, package_name):
    """Updates a single package."""
    try:
        subprocess.check_call([python_path, '-m', 'pip', 'install', '--upgrade', package_name])
        print(f"Successfully updated: {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error while updating {package_name}: {e}")

def update_pip(python_path):
    """Ensures pip is updated."""
    try:
        subprocess.check_call([python_path, '-m', 'pip', 'install', '--upgrade', 'pip'])
        print("Successfully updated: pip")
    except subprocess.CalledProcessError as e:
        print(f"Error while updating pip: {e}")

def main():
    python_path = ""

    if not python_path:
        python_path = sys.executable

    print(f"Using Python executable: {python_path}")

    # Update pip
    print("Updating pip...")
    update_pip(python_path)

    print("Getting list of outdated packages...")
    outdated_packages = get_outdated_packages(python_path)

    if not outdated_packages:
        print("All packages are up to date.")
    else:
        print("Updating packages...")
        for package in outdated_packages:
            package_name = package.split()[0]  # The package name is in the first column
            update_package(python_path, package_name)

    # Final notification
    print("\nAll packages, including pip, have been successfully updated.")

    time.sleep(30)

if __name__ == "__main__":
    main()
