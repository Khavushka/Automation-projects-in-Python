# Automating web scrapping
# Installing necessary libraries
# pip install requests
# pip install beautifulsoup4

import requests from bs4 
import BeautifulSoup

# Writing the automation script

url = 'https://www.python.org/'
output_file = 'python_articles.txt'
response = requests.get(url) 
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')
                         
with open(output_file, 'w') as f:
 for article in articles:
 title = article.h1.text.strip()
 f.write(title + '\n')

# script that extracts the titles of all articles on the Python.org website 
# and saves them to a file