import requests

url = 'https://api.pwnedpasswords.com/range/' + 'e6b6a'
res = requests.get(url)
print(res)

def request_api_data(query_char):
    pass

def pwned_api_check(password):
    #check password if it exists in API response
    pass