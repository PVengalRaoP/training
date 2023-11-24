import requests

def get_usd_to_inr():
    response = requests.get('https://open.er-api.com/v6/latest/USD')
    data = response.json()
    inr_rate = data['rates']['INR']
    return inr_rate

usd_amount = float(input("Enter the amount in USD: "))
conversion_rate = get_usd_to_inr()
inr_amount = usd_amount * conversion_rate

print(f"{usd_amount} USD is approximately {inr_amount:.2f} INR at the current rate.")

