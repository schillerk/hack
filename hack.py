from lxml import html
import requests

page = requests.get('https://www.soylent.com/')
print page.content

import indico

indicoio.config.api_key = '246290703649a7500961ea78369dbce8'