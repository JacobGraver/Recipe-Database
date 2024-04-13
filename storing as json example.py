import json

# Dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Serialize dictionary to JSON string
json_str = json.dumps(my_dict)

# Write JSON string to a file
with open('data.json', 'w') as f:
    f.write(json_str)

# Later, deserialize JSON string back to dictionary
with open('data.json', 'r') as f:
    loaded_dict = json.load(f)

print(loaded_dict)
