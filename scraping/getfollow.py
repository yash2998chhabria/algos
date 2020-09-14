import requests 
from bs4 import BeautifulSoup
import json


instagram_url = 'https://www.instagram.com'
profile_url = 'mizz_shk'

response = requests.get(f"{instagram_url}/{profile_url}")
#print(response.status_code)
if response.ok:
    html = response.text
    bs_html = BeautifulSoup(html , 'lxml')
    #scripts = bs_html.select('script[type="application/Id+json"]')
    script = bs_html.find('script', type='application/ld+json').string
    script_content = json.loads(script.strip())
    #print(json.dumps(script_content, indent=4, sort_keys=True))
    followers_count = script_content['mainEntityofPage']['interactionStatistic']['userInteractionCount']
    print(followers_count)
    additional = bs_html.findAll('script')
    #print(additional[4])
    print(json.dumps(additional[4].string, indent=4, sort_keys=True))