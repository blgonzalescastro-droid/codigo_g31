import requests
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

users = response.json()

users = [
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'johndoe@example.com'
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'email': 'janesmith@example.com'
    }
]

flag = True