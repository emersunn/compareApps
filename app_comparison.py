#!/usr/bin/env python3

import os
import subprocess
import sys

# Function to get the list of installed applications on a MacOS computer
def get_installed_apps():
    apps = []
    # Define the directories where applications are typically installed
    app_directories = ['/Applications', '~/Applications']

    # Iterate through the app directories
    for directory in app_directories:
        # Expand user directory (~) and check if the path exists
        if os.path.exists(os.path.expanduser(directory)):
            # Iterate through the files and folders in the directory
            for app in os.listdir(os.path.expanduser(directory)):
                # Check if the item is an application (ends with .app)
                if app.endswith('.app'):
                    # Add the application to the list of apps
                    apps.append(app)

    # Return the sorted list of installed applications
    return sorted(apps)

# Function to save the list of installed applications to a file
def save_list_to_file(filename, app_list):
    with open(filename, 'w') as f:
        for app in app_list:
            # Write each application to the file, one per line
            f.write(f'{app}\n')

# Function to read the list of applications from a file
def read_list_from_file(filename):
    with open(filename, 'r') as f:
        # Read the file and return a list of applications, stripping any whitespace
        return [line.strip() for line in f.readlines()]

# Function to compare two lists of installed applications
def compare_app_lists(old_apps, new_apps):
    # Determine added apps by subtracting the set of old apps from the set of new apps
    added_apps = set(new_apps) - set(old_apps)
    # Determine removed apps by subtracting the set of new apps from the set of old apps
    removed_apps = set(old_apps) - set(new_apps)

    return added_apps, removed_apps

def main():
    if len(sys.argv) != 3:
        print('Usage: ./app_comparison.py <old_apps_file> <new_apps_file>')
        sys.exit(1)

    # Get the file names from the command line arguments
    old_apps_file = sys.argv[1]
    new_apps_file = sys.argv[2]

    # Get the list of installed applications on the new computer
    new_apps = get_installed_apps()
    # Save the list of new applications to the specified file
    save_list_to_file(new_apps_file, new_apps)

    # Check if the old apps file exists
    if not os.path.exists(old_apps_file):
        print(f'Old apps file "{old_apps_file}" not found. Cannot compare.')
        sys.exit(1)

    # Read the list of old applications from the specified file
    old_apps = read_list_from_file(old_apps_file)
    # Compare the old and new application lists
    added_apps, removed_apps = compare_app_lists(old_apps, new_apps)

    # Output the added and removed applications
    print('Added apps:')
    for app in sorted(added_apps):
        print(f'  - {app}')

    print('\nRemoved apps:')
    for app in sorted(removed_apps):
        print(f'  - {app}')

if __name__ == '__main__':
    main()
