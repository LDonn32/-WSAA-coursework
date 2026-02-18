import requests

#  making a GET request
r = requests.get('https://www.cso.ie/en/index.html')

# check status code
print(r.status_code)

