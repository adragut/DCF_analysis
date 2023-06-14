import requests
import json

# Set up API endpoint URL
base_url = 'https://seeking-alpha.p.rapidapi.com/'
endpoint_url = base_url + 'symbols/get-financials'

headers = {'X-RapidAPI-Key':'6a1269eb60msh80257fe6797736cp147a07jsnb276f98fded5',
    'X-RapidAPI-Host':'seeking-alpha.p.rapidapi.com'
}

# Retrieve target stock ticker and desired currency
stock_ticker = input("Enter the target stock ticker: ")
period_type = input("One of the following : annual|quarterly|ttm")
statement_type = input("One of the following : income-statement|balance-sheet|cash-flow-statement")
target_currency = input("Enter target currency: USD or e.g. EUR\n")
if target_currency not in ["USD", "EUR"]:
    print('Error: Invalid currency')
else:
    target_currency = target_currency.upper()

# Format Rapid API request payload with necessary parameters
payload = {'symbol': f'{stock_ticker}','target_currency':f'{target_currency}','period_type':f'{period_type}','statement_type':f'{statement_type}'}
if target_currency != 'USD':
    payload['foreign_exchange'] = True

# Send GET request to retrieve data
response = requests.get(endpoint_url, params=payload, headers=headers)

if response.status_code == 200:
    # Parse json response
    json_data = response.json()
    
    #Path JSON 
    file_path = 'C:\\Users\\alexandru.dragut\\Documents\\response.json'  # Replace with the desired file path

    # Save JSON response to the specified file path
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)
        print(f'JSON response saved to {file_path}') 
else:
    # Handle errors
    print('Unexpected status code: {}'.format(response.status_code))

# Print response JSON object
# print(response.json())