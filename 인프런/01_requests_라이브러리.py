import requests

response = requests.get("http://www.kgaasset.co.kr/index.asp")
html = response.text

print(html)
