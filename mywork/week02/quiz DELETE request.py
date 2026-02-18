


from urllib import response
import requests
# Basic DELETE request
r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
r.raise_for_status()
print(r.status_code)