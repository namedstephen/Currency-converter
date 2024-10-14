import requests

user_currency = input("Enter your currency (USD) : ").upper()
target_currency = input("Enter target currency (EUR) : ").upper()
amonut = float(input("Enter amount : "))
response = requests.get(f"https://v6.exchangerate-api.com/v6/039e7a45a3f6611a54438450/latest/{user_currency}")
target_rate = response.json()["conversion_rates"][target_currency]
converted_amount = amonut * target_rate
print("Converted amount: ", converted_amount, target_currency)


# ============= api request=======================
# import requests

# def scrap(name):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
#     print(response.json()["name"].capitalize())
# scrap('pikachu')
