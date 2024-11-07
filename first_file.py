import requests

root_url = "https://country-leaders.onrender.com" 
status_url = "status"
req = requests.get(f"{root_url}/{status_url}")

if req.status_code == 200:    
    print(req.text) 
else:
    print(f"Error to access the website: {req.status_code}") 

#countries
countries_url = "countries"
req = requests.get(f"{root_url}/{countries_url}")
countries = req.json()
#print(countries)

#cookie
cookie_url = "cookie"    
cookie = requests.get(f"{root_url}/{cookie_url}").cookies
r = requests.get(f"{root_url}/{countries_url}", cookies=cookie)
countries = r.json()

#leaders
leaders_url = 'leaders'
leaders_per_country = {}
for country in countries:        
    leader = requests.get(f"{root_url}/{leaders_url}", cookies=cookie, params={"country":country})        
    leaders_per_country[country] = leader.json()
#print (leaders_per_country)