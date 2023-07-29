import mappyfile
import yaml
import json
import os

def get_templates_folder():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")

def load_string_to_yaml(yaml_string):
    try:
        # Load the YAML string into a Python data structure
        yaml_data = yaml.safe_load(yaml_string)
        return yaml_data
    except yaml.YAMLError as e:
        print(f"Error loading YAML: {e}")
        return None

def load_yaml(file_path):

    # Load the YAML string into a Python data structure (dictionary in this case)

    # Load YAML data from the file
    with open(file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        
    return data


def _update_layers(m, yaml_data):

    for l in m["layers"]:
        mappyfile.update(l, yaml_data["layers"], overwrite=False)
        if "styles" in l and "styles" in yaml_data:
            for c in l["classes"]:
                mappyfile.update(c, yaml_data["classes"], overwrite=False)
                if "styles" in c and "styles" in yaml_data:
                    for s in c["styles"]:
                        mappyfile.update(s, yaml_data["styles"], overwrite=False)

def apply(m, template_key: str="wms", add_example_layer: bool = False):

    # print(json.dumps(m, indent=4))

    template_path = os.path.join(get_templates_folder(), f"{template_key}.yml")

    yaml_data = load_yaml(template_path)
    mappyfile.update(m, yaml_data["map"], overwrite=False)

    if "layers" not in m or len(m["layers"]) == 0:
        if "layers" in yaml_data and add_example_layer:
            m["layers"] = [{"__type__": "layer"}]

    if "layers" in m and "layers" in yaml_data:
        _update_layers(m, yaml_data)

    return m

