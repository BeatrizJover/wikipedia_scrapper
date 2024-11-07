import requests

def get_leaders():
    '''Fetches and returns a dictionary of country leaders from an external API.'''

    #Checks the status of the API
    root_url = "https://country-leaders.onrender.com" 
    status_url = "status"
    req = requests.get(f"{root_url}/{status_url}")
    if req.status_code == 200:    
        print(req.text) 
    else:
        print(f"Error to access the website: {req.status_code}") 
        
    #retrieves a session cookie and a list of countries
    countries_url = "countries"
    cookie_url = "cookie"    
    cookie = requests.get(f"{root_url}/{cookie_url}").cookies
    r = requests.get(f"{root_url}/{countries_url}", cookies=cookie)
    countries = r.json()
    
    # fetches the leaders and stores the data in a dictionary 
    leaders_url = 'leaders'
    leaders_per_country = {}
    for country in countries:        
            leader = requests.get(f"{root_url}/{leaders_url}", cookies=cookie, params={"country":country})        
            leaders_per_country[country] = leader.json()
    return leaders_per_country

# test = get_leaders()
# print(test)