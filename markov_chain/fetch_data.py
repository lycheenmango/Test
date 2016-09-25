""" This is my first project after completing the Code Academy Python course. The aim 
is to be able to generate a bunch of lyrics based on the lyrics of my favorite artist(s)

Project has three areas that I will cover: 
- Fetch data from the web; remove any non-text data such as HTML tags.
- Create the Markov chain with clean text data.
- Generate and display text using the Markov chain (more on this later).

*** NOTE*** The code isn't complete yet, this is just the skeleton code that I intend to keep iterating on.
"""

"""
1. Open html pages to get text from online sources
2. Parse through the text, remove html tags and add the data to a variable
3. Ensure this is clean data
"""

from bs4 import BeautifulSoup
import urllib2
#import requests
from markov_python.cc_markov import MarkovChain

url = "http://www.azlyrics.com/lyrics/script/halloffame.html"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")
lyrics = soup.get_text()
lyrics = str(lyrics)
#print lyrics
#response  = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
#soup = BeautifulSoup(response.txt, "lxml")
#print soup.prettify()
#print soup.get_text()
#lyrics = soup.find_all("div", class_ = "lyricsh")
#print lyrics


""" 
Use Code Academy code to build the markov chains with this clean data
"""
mc = MarkovChain()
mc.add_string(lyrics)


"""
Generate and display text using the Markov chain
"""
output = mc.generate_text()
print output
