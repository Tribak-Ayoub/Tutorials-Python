import requests

def submit_contact_form():
    url = "https://httpbin.org/post"
    data = {
        'name': input('your name: '),
        'email': input('your email: '),
        'message': input('your message: ')
    }

    response = requests.post(url, json=data)

    if response.ok:
        result = response.json()
        print("\n Server received the following data:")
        for key, value in result.items():
            print(f'{key}: {value}')
    else:
        print('Submission failed')

submit_contact_form()