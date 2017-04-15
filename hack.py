from lxml import html
import requests
import indicoio

indicoio.config.api_key = '246290703649a7500961ea78369dbce8'

page = requests.get('https://www.soylent.com/')
content = page.content

print indicoio.keywords(content)
print content