# /// script
# dependencies = [
#   "jinja2",
#   "pyyaml",
# ]
# ///

import yaml
from jinja2 import Environment, FileSystemLoader
import os

def main():
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'riccs_favorites.yaml')
    template_dir = os.path.join(base_dir, 'templates')
    output_path = os.path.join(base_dir, 'index.html')

    # Read Data
    with open(data_path, 'r') as f:
        data = yaml.safe_load(f)

    # Setup Jinja2
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('index.html')

    # Render
    output = template.render(data=data)

    # Write Output
    with open(output_path, 'w') as f:
        f.write(output)

    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
