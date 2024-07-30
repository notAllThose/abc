import yaml

def sort_openapi_schemas(input_file, output_file):
    # Load the OpenAPI YAML file
    with open(input_file, 'r', encoding='utf-8') as f:
        openapi_data = yaml.safe_load(f)
    
    # Check if components and schemas exist in the YAML structure
    if 'components' in openapi_data and 'schemas' in openapi_data['components']:
        schemas = openapi_data['components']['schemas']

        # Sort the schemas alphabetically
        sorted_schemas = dict(sorted(schemas.items()))
        
        # Update the OpenAPI data with sorted schemas
        openapi_data['components']['schemas'] = sorted_schemas
    
    # Write the sorted OpenAPI data back to a YAML file
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(openapi_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

sort_openapi_schemas('hrwYaml.yaml', 'sorted_openapi.yaml')
