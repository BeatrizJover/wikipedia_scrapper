import requests
from bs4 import BeautifulSoup
from main_function import get_leaders

def fetch_leader_wikipedia_text(leaders_data):    
    '''get the wikipedia url of the first leader'''
    return next(iter(leaders_data.values()))[0].get("wikipedia_url")

# fetch wiki text
wiki_url = fetch_leader_wikipedia_text(get_leaders())
response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

for paragraph in soup.find_all('p'):
    print(paragraph.text)


