#!/usr/bin/env python3

import subprocess

# Get a list of user-installed packages
dpkg_output = subprocess.check_output(["dpkg", "-l"]).decode("utf-8").splitlines()

# Initialize a list to store package information
package_info = []

# Get the total number of packages
total_packages = sum(1 for line in dpkg_output if line.startswith("ii"))

# Initialize a counter
package_count = 0

# Iterate through the dpkg output
for line in dpkg_output:
    parts = line.split()
    if len(parts) >= 3 and parts[0] == "ii":
        package_name = parts[1]
        package_version = parts[2]
        package_description = " ".join(parts[3:])
        
        # Check if the package is manually installed (user-installed)
        is_manually_installed = subprocess.check_output(["apt-mark", "showmanual", package_name]).decode("utf-8").strip() == package_name

        if is_manually_installed:
            # Append package information to the list
            package_info.append({
                "Package": package_name,
                "Version": package_version,
                "Description": package_description,
            })

    # Update the package count and display progress
    package_count += 1
    print(f"Processing package {package_count}/{total_packages}...", end="\r")

# Write package information to a CSV file
with open("user_installed_packages.csv", "w") as output_file:
    # Write column headers
    output_file.write("Package,Version,Description\n")
    
    # Write package data
    for info in package_info:
        output_file.write(f"{info['Package']},{info['Version']},{info['Description']}\n")

# Print a completion message
print("\nPackage list generation completed.")
