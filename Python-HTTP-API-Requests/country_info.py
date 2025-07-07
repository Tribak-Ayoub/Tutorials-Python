import requests

def get_country_info(country):
    url = f"https://restcountries.com/v3.1/name/{country}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()[0]
        print(f"\n🌍 Country: {data['name']['common']}")
        print(f"🏙️ Capital: {data['capital'][0]}")
        print(f"👥 Population: {data['population']:,}")
        print(f"💱 Currency: {list(data['currencies'].keys())[0]}")
        print(f"📍 Region: {data['region']}")
    except requests.exceptions.HTTPError as err:
        print('HTTP error: ', err)
    except Exception as e:
        print("Other error:", e)

country = input('Enter country name: ')
get_country_info(country)