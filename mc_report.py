import requests

# Define the URL with query parameters
url = f"https://one9-mc.onrender.com/api/expense/stats/report?startDate=2025-01-01&endDate=2025-01-19&frequency=weekly"

try:
    print('Sending request.')
    # Make the GET request
    response = requests.get(url)

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Parse the response JSON
    data = response.json()
    print("Response Data:", data)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
