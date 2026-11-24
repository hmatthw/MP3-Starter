users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}
]

# Print only the users who have the role "admin" via a loop

for i in users:
    try:
        if i['role'] == 'admin':
           print(i['name'])
    except KeyError:
        continue