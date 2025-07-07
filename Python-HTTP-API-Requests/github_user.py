import requests

def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        user = response.json()
        print(f"Username: {user['login']}")
        print(f"Name: {user.get('name', 'No name')}")
        print(f"Location: {user.get('location', 'Unknown')}")
        print(f"Avatar: {user['avatar_url']}")
        print(f"Public Repos: {user['public_repos']}")
        print(f"Followers: {user['followers']}")
    else:
        print('not found')

username = input('Enter Github username: ')
get_github_user(username)