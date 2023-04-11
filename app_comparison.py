#!/usr/bin/env python3

import os
import subprocess
import sys

# Function to get the list of installed applications on a MacOS computer
def get_installed_apps():
    apps = []
    app_directories = ['/Applications', '~/Applications']

    for directory in app_directories:
        if os.path.exists(os.path.expanduser(directory)):
            for app in os.listdir(os.path.expanduser(directory)):
                if app.endswith('.app'):
                    apps.append(app)

    return sorted(apps)

# Function to save the list of installed applications to a file
def save_list_to_file(filename, app_list):
    with open(filename, 'w') as f:
        for app in app_list:
            f.write(f'{app}\n')

# Function to read the list of applications from a file
def read_list_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Function to compare two lists of installed applications
def compare_app_lists(old_apps, new_apps):
    added_apps = set(new_apps) - set(old_apps)
    removed_apps = set(old_apps) - set(new_apps)

    return added_apps, removed_apps

def main():
    if len(sys.argv) != 3:
        print('Usage: ./app_comparison.py <old_apps_file> <new_apps_file>')
        sys.exit(1)

    old_apps_file = sys.argv[1]
    new_apps_file = sys.argv[2]

    new_apps = get_installed_apps()
    save_list_to_file(new_apps_file, new_apps)

    if not os.path.exists(old_apps_file):
        print(f'Old apps file "{old_apps_file}" not found. Cannot compare.')
        sys.exit(1)

    old_apps = read_list_from_file(old_apps_file)
    added_apps, removed_apps = compare_app_lists(old_apps, new_apps)

    print('Added apps:')
    for app in sorted(added_apps):
        print(f'  - {app}')

    print('\nRemoved apps:')
    for app in sorted(removed_apps):
        print(f'  - {app}')

if __name__ == '__main__':
    main()
