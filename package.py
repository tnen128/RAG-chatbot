import pkg_resources

def print_installed_versions(requirements_file):
    try:
        with open(requirements_file, 'r') as file:
            packages = [line.strip().split('==')[0] for line in file if line.strip()]
        
        print(f"{'Package':<30} {'Installed Version':<20}")
        print("=" * 50)
        
        for package in packages:
            try:
                version = pkg_resources.get_distribution(package).version
                print(f"{package:<30} {version:<20}")
            except pkg_resources.DistributionNotFound:
                print(f"{package:<30} Not Installed")
    except FileNotFoundError:
        print(f"The file {requirements_file} does not exist.")

# Specify the path to your requirements.txt file
requirements_file = 'requirements.txt'
print_installed_versions(requirements_file)
