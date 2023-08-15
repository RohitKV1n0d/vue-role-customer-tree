def create_hierarchy_tree(data_list):
    root = {}

    # Helper function to insert the node in the hierarchy
    def insert_node(node):
        current = root
        for part in node["path"][:-1]:  
            if part not in current:
                current[part] = {"name": part, "children": {}}
            current = current[part]["children"]

        current[node["name"]] = node

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

def generate_trees(data):
    # Split data into different lists based on root node
    roots = {}
    for item in data:
        root_name = item["path"][0]
        if root_name not in roots:
            roots[root_name] = []
        roots[root_name].append(item)

    # For each root-based list, create hierarchy tree
    result = []
    for root_list in roots.values():
        tree = create_hierarchy_tree(root_list)
        result.append(tree)

    return result

# Test
data_list = [
    {"name": "Category 1", "path": ["Category 1"], "level": 0, "children": {}},
    {"name": "Category 2", "path": ["Category 1", "Category 2"], "level": 1, "children": {}},
    {"name": "Category 3", "path": ["Category 1", "Category 2", "Category 3"], "level": 2, "children": {}},
    {"name": "Category 4", "path": ["Category 1", "Category 2", "Category 4"], "level": 2, "children": {}},
    {"name": "Category 11", "path": ["Category 11"], "level": 0, "children": {}},
    {"name": "Category 22", "path": ["Category 11", "Category 22"], "level": 1, "children": {}},
    {"name": "Category 33", "path": ["Category 11", "Category 22", "Category 33"], "level": 2, "children": {}},
    {"name": "Category 44", "path": ["Category 11", "Category 22", "Category 44"], "level": 2, "children": {}}
]

result = generate_trees(data_list)

print(result)


{"name": "Category 1", "path": ["Category 1"], "level": 0, "children": {"0": {"name": "Category 2", "path": ["Category 1", "Category 2"], "level": 1, "children": {"0": {"name": "Category 3", "path": ["Category 1", "Category 2", "Category 3"], "level": 2, "children": {}}, "1": {"name": "Category 4", "path": ["Category 1", "Category 2", "Category 4"], "level": 2, "children": {}}}}}}
{'name': 'Category 11', 'path': ['Category 11'], 'level': 0, 'children': {'0': {'name': 'Category 22', 'path': ['Category 11', 'Category 22'], 'level': 1, 'children': {'0': {'name': 'Category 33', 'path': ['Category 11', 'Category 22', 'Category 33'], 'level': 2, 'children': {}}, '1': {'name': 'Category 44', 'path': ['Category 11', 'Category 22', 'Category 44'], 'level': 2, 'children': {}}}}}}