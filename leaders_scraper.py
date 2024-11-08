from bs4 import BeautifulSoup
from requests import Session
import time
import json
import re

def session_loop_request(session, url, cookies=None, params=None, retry=False):    
    response = session.get(url, cookies=cookies, params=params)
    if response.status_code == 403 and not retry:       #this fix the cookie expired problem  
        print("Cookie expired. Refreshing cookie and retrying...")
        new_cookie = refresh_cookie(session)
        return session_loop_request(session, url, cookies=new_cookie, params=params, retry=True)
    response.raise_for_status()
    if "json" in response.headers.get("Content-Type", ""):
        return response.json()
    return response.text

def refresh_cookie(session): #this fix the cookie expired problem    
    root_url = "https://country-leaders.onrender.com"
    cookie_url = f"{root_url}/cookie"
    return session.get(cookie_url).cookies

def get_leaders():
    root_url = "https://country-leaders.onrender.com"    
    with Session() as session:        
        status_url = f"{root_url}/status"
        status_response = session.get(status_url)
        if status_response.status_code == 200:
            print(status_response.text)
        else:
            print(f"Error accessing the website: {status_response.status_code}")        
        cookie = refresh_cookie(session)
        countries_url = f"{root_url}/countries"
        countries = session_loop_request(session, countries_url, cookies=cookie)        
        leaders_per_country = {}
        leaders_url = f"{root_url}/leaders"
        for country in countries:
            country_leaders = {}
            leaders_data = session_loop_request(session, leaders_url, cookies=cookie, params={"country": country})            
            for leader in leaders_data:
                full_name = f"{leader.get('first_name')} {leader.get('last_name')}"
                wikipedia_url = leader.get('wikipedia_url')
                if wikipedia_url:                    
                    first_paragraph = get_first_paragraph(session, wikipedia_url)
                    country_leaders[full_name] = first_paragraph
                    print(f"Leader of {country}: {full_name}, First Paragraph: {first_paragraph}")            
            leaders_per_country[country] = country_leaders
            time.sleep(0.5)  # delay between countries to avoid overload
            
    return leaders_per_country

def get_first_paragraph(session, wikipedia_url):    
    print(wikipedia_url)
    response = session.get(wikipedia_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    first_paragraph = None
    for paragraph in paragraphs:
        text = paragraph.get_text(separator=" ",strip=True)# this fix the words problem
        if text:
            first_paragraph = text
            break 

    if first_paragraph: 
        first_paragraph = re.sub(r'\(\[\s?.*?\s?\]\s?\/.*?;?\)|\[\s?[a-zA-Z0-9]\s?\]', '', first_paragraph) #this fix refefences[1],[a]
       
    return first_paragraph

# Test:
leaders_data = get_leaders()

def save(leaders_per_country):
    with open('leaders.json', 'w') as json_file:  
        json.dump(leaders_per_country, json_file, indent=4) 

save(leaders_data)

