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

# all paragraph
paragraphs = soup.find_all('p')

#get the 1st paragraph
intro_paragraph = None
for paragraph in paragraphs: 
    text = paragraph.get_text(strip=True) #check non-empty paragraphs
    if text:  
        intro_paragraph = text
        break

print(intro_paragraph)


