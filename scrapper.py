import requests
from bs4 import BeautifulSoup
user  = raw_input("Enter Username: ");
url = "https://www.codechef.com/users/%s" %(user) 
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

for i in soup.find_all("div",{ "class" : "rating-number"}):
    	print(i.text)



