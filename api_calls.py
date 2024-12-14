import requests
from secret_keys import client_id, client_secret

# Get access token
url = "https://api.intra.42.fr/oauth/token"
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(url, data=data)

# Check if access token was successfully retrieved
if response.status_code == 200:
    access_token = response.json().get('access_token')
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # API call to fetch user data
    user_url = "https://api.intra.42.fr/v2/users/mvelazqu/locations_stats.json"  # Replace with an actual username
    user_response = requests.get(user_url, headers=headers)

    # Check if the API call was successful
    if user_response.status_code == 200:
        user_data = user_response.json()
        print(user_data)
    else:
        print(f"Failed to fetch user data. Status code: {user_response.status_code}")
        print(user_response.text)
else:
    print(f"Failed to retrieve access token. Status code: {response.status_code}")
    print(response.text)
