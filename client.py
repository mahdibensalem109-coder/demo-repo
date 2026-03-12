import requests

# The URL where your FastAPI server is running
url = "http://127.0.0.1:8000/calculate"

# The data we want to send (must match your Pydantic model)
payload = {
    "num1": 10.5,
    "num2": 2,
    "operator": "*"
}

# response = requests.get('http://127.0.0.1:8000/hello',json=payload)
# data = response.json()
# print(data["message"])

try:
    # Sending the POST request
    response = requests.post(url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print(f"Success! {data['operation']} = {data['result']}")
        print(response.status_code)
    else:
        print(f"Error {response.status_code}: {response.text}")

except requests.exceptions.ConnectionError:
    print("Connection failed. Is your FastAPI server running?")

"hghghg"