# Simple Tor Proxy Chain Using Python
# Credit /D/ 

import requests

# Do not Change
tor_proxy = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Target URL
target_url = 'http://example.com'

# Function 
def send_request(url, proxy):
    try:
        # Send HTTP GET request using Tor proxy
        response = requests.get(url, proxies=proxy)
        # Print response from Tor proxy
        print(f"Response from Tor proxy: {response.status_code}")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function 
send_request(target_url, tor_proxy)
