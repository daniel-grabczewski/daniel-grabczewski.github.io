import os
import yaml
import shutil
from datetime import datetime

# Define the path to your YAML data file
DATA_FILE = '_data/project-pages.yml'
# Define the output directory for generated Markdown files
OUTPUT_DIR = '_projects'
# Define the backup directory
BACKUP_DIR = '_project-page-backups'

def main():
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Ensure the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # Load the project data from the YAML file
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        projects = yaml.safe_load(f)

    for project in projects:
        # Use the 'slug' field as the filename
        filename = f"{project['slug']}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Check if the file already exists
        if os.path.isfile(filepath):
            # Get the current timestamp in the format dd-mm-yyyy-hh-mm-am/pm
            timestamp = datetime.now().strftime('%d-%m-%Y-%I-%M-%p')
            # Define the backup filename with timestamp
            backup_filename = f"{os.path.splitext(filename)[0]}-{timestamp}.md"
            backup_filepath = os.path.join(BACKUP_DIR, backup_filename)
            # Move the existing file to the backup directory
            shutil.move(filepath, backup_filepath)
            print(f"Backed up {filepath} to {backup_filepath}")

        # Start building the front matter
        front_matter = {'layout': 'project'}
        front_matter.update(project)  # Add all project fields to the front matter

        # Convert the front matter dictionary to YAML format
        front_matter_yaml = yaml.dump(front_matter, default_flow_style=False, sort_keys=False, allow_unicode=True)

        # Build the content of the Markdown file
        content = f"---\n{front_matter_yaml}---\n"

        # Write the content to the Markdown file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Generated {filepath}")

if __name__ == "__main__":
    main()
