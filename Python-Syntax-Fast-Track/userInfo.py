import requests

def get_user_info():
    username = input('Enter github username:')
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        name = user_data.get('name') or "No name provided"
        avatar_url = user_data.get('avatar_url')

        print(f"👋 GitHub User: {username}")
        print(f"Name: {name}")
        print(f"Profile Image URL: {avatar_url}")
    else:
        print(f"User '{username}' not found. Please check the username and try again.")
        
get_user_info()