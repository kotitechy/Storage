import subprocess

def list_installed_packages():
    i=0
    try:
        # Run the pip list command
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        # Print the output
        print(result.stdout)

    except FileNotFoundError:
        print("Error: pip is not installed or not accessible.")

# Call the function to list installed packages
list_installed_packages()
