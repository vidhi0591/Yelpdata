!pip install beautifulsoup4
from requests import get
from bs4 import BeautifulSoup
url = 'https://www.yelp.com/search?find_desc=Happy%20Hour&find_loc=San%20Mateo%2C%20CA&start=0'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
