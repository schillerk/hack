from lxml import html
import requests
import indico

indicoio.config.api_key = '246290703649a7500961ea78369dbce8'

page = requests.get('https://www.soylent.com/')

indicoio.keywords(page.content)
