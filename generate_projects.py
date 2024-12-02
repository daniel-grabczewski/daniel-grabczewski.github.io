import os
import yaml

# Define the path to your YAML data file
DATA_FILE = '_data/project-pages.yml'
# Define the output directory for generated Markdown files
OUTPUT_DIR = '_projects'

def main():
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Load the project data from the YAML file
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        projects = yaml.safe_load(f)

    for project in projects:
        # Use the 'slug' field as the filename
        filename = f"{project['slug']}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

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
