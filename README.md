# MacOS App Comparison Script

This Python script compares the installed applications on two MacOS computers. It generates a list of installed applications for the old and new computers and compares them to identify added and removed apps.

## Usage

1. Run the script on the old computer and provide a file name for the old_apps file:
```
./app_comparison.py old_apps.txt new_apps.txt
```
2. Transfer the old_apps.txt file to the new computer.

3. Run the script on the new computer and provide the file names for the old_apps_file and new_apps_file:
```
./app_comparison.py old_apps.txt new_apps.txt
```
The script will output the added and removed applications in the terminal.

## Dependencies
- Python 3.x
