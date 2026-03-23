import requests
import urllib.parse
from config import apikeys as cfg

targetUrl = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html"

apiKey = cfg["htmltopdfkey"]

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl, 'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl + "?" + parsedparams

response = requests.get(requestUrl)
print(response.status_code)

result = response.content