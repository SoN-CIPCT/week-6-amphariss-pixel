#Conditional list
web_users = ['megan', 'abby', 'dylan', 'wyatt', 'liam']
new_users = ['megan', 'abby', 'bernice', 'monica', 'aaron']

for user in new_users:
    if user in web_users:
        print(f"This user name is already in use: {user}.")
    else:
        print(f"This user name is available: {user}.")

#Dictionary
cities = {
    "Seattle": {
        "country": "United States",
        "population": 750000,
        "fact": "Seattle won the 2026 Super Bowl."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Tokyo is the largest city in the world."
    },
    "Naples": {
        "country": "Italy",
        "population": 970000,
        "fact": "Naples created the pizza."
    }
}
for city, info in cities.items():
    print(f"{city}, {info['country']}, {info['population']}, {info['fact']}") 
