import requests
from datetime import date

try:
    print('Sending request.')
    today = date.today()
    startDate = f"{today.year}-{today.month}-01"
    if(today.month==1):
        startDate = f"{today.year-1}-12-28"
    else:
        startDate = f"{today.year}-{today.month-1}-28"
    frequency = 'weekly'
    if(today.day==7 or today.day==14):
        frequency='daily'
    # Make the GET request
    url = f"https://one9-mc.onrender.com/api/expense/stats/report?startDate={startDate}&endDate={today}&frequency={frequency}"
    response = requests.get(url)

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Parse the response JSON
    data = response.json()
    print("Response Data:", data)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
