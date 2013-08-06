#  install BeutifulSoup first
# you can do this by: pip install beautifulsoup4
from bs4 import BeautifulSoup
import urllib2

page_url = "https://github.com/CodeCatz/litterbox/commits/master"
content = urllib2.urlopen(page_url)

soup = BeautifulSoup(content)
commits = soup.findAll('li','commit')

# prints authors and commit messages on litterbox master
for commit in commits:
	print commit.find('span','author-name').get_text().strip()
	print commit.find('a','message').get_text().strip()
	print '-----------------------------------------------------'
