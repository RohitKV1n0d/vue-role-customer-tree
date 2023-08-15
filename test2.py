import copy

def create_hierarchy_tree(data_list):
    root = {}

    # Helper function to insert the node in the hierarchy
    def insert_node(node):
        current = root
        for part in node["path"][:-1]:  # Exclude the last part of the path because we'll insert it at the end
            if part not in current:
                # If not present, initialize a minimal node
                current[part] = {"username": part, "children": {}}
            current = current[part]["children"]

        # Insert the actual node
        current[node["username"]] = node

    for entry in data_list:
        insert_node(entry)

    # Flatten the structure
    def flatten(node):
        children = {str(idx): child for idx, child in enumerate(node["children"].values())}
        node["children"] = children
        for child in children.values():
            flatten(child)
        return node

    return flatten(root[list(root.keys())[0]])

# Sample Data
hierarchy_import_data_list = [
    {
        "username": "CEO1",
        "path": ["CEO1"],
        "role": 0,
        "children": {},
        "enabled": True,
        "firstName": "CEO",
        "lastName": "1",
        "email": "ceo@sample.co",
        "password": "ceo",
        "phone": "1234567890",
        "address": "ceo address",
        "state": "ceo state",
        "pan": "ceo pan",
        "region": "ceo region",
        "uuid": "sample_uuid"
    },
    {
        "username": "Manager 1",
        "path": ["CEO1", "Manager 1"],
        "role": 1,
        "children": {},
        "enabled": True,
        "firstName": "Manager",
        "lastName": "1",
        "email": "manager1@sample.co",
        "password": "manager",
        "phone": "1234567890",
        "address": "manager address",
        "state": "manager state",
        "pan": "manager pan",
        "region": "manager region",
        "uuid": "sample_uuid2"
    }
]

result = create_hierarchy_tree(hierarchy_import_data_list)
print(result)