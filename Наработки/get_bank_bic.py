import requests

def get_bank_bic(account_number):
    url = f'https://www.cbr.ru/fininfo/credit/req?ACCOUNT={account_number}'
    try:
        response = requests.get(url)
        data = response.json()
        if 'bic' in data:
            return data['bic']
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


print(get_bank_bic('30101810745374525104'))