import requests

url = 'https://api.exchangerate.host/convert'
response = requests.get(url, params = {
    "from": input('Enter from currency code: ').upper(),
    "to": input('Enter to currency code: ').upper(),
    "amount": input('Enter Amount: ')
})
data = response.json()['result']

print(f"Converted amount: {data}")