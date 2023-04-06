import requests
import html2text

url = input('Paste URL')

response = requests.get(url)

content = response.text

if content.find('<title>') != -1:
    title1=content.partition('<title>')[2]
    title=title1.partition('</title>')[0]
    print(title)

print(content)


