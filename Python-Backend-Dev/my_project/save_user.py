import json

def save_user():
    name = input('Name: ')
    age = input('Age: ')
    user = {'name': name, 'age': age}

    with open('user.json', 'w') as f:
        json.dump(user, f)
    print('saved')

def read_user():
    with open('user.json', 'r') as f:
        data = json.load(f)
        print(f'Hello {data['name']}, age {data['age']}')

save_user()
read_user()
