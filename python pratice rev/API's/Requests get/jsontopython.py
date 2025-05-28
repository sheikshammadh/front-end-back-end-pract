import json

# Example JSON data (as a string)
json_data = '''
{
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
'''

# Parse JSON string to Python dictionary
data = json.loads(json_data)

# Access data in Python
print(data)
print("Name:", data["name"])
print("Age:", data["age"])
print("Email:", data["email"])