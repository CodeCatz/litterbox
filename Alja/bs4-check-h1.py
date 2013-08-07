
# Playing with BeautifulSoup, whoop!
# This is just a silly example that looks for the first string tag
# And then writes all h1 titles
# A good check if people actually use h1 properly

from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError
import re

page_url = "http://blog.ialja.com"

user_url = raw_input('Which page do you want to check?\n')

while not(re.match(r'https?://', user_url)):
	user_url = raw_input('Type in a link beginning with http://\n')

# just checking if the url is working
# code borrowed from http://stackoverflow.com/questions/11983049/python-read-and-validate-input-url
req = Request(user_url)
try:
    response = urlopen(req)
except URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print "\n-----\n"
        #print 'Reason: ', e.reason
        print "I'll just give you an example with %s" % page_url
        page_content = urlopen(page_url)
    elif hasattr(e, 'code'):
        print 'Sorry, couldn\'t reach that server.'
        print "\n-----\n"
        #print 'Error code: ', e.code
        print "I'll just give you an example with %s" % page_url
        page_content = urlopen(page_url)
else:
    page_content = response
    page_url = user_url



soup = BeautifulSoup(page_content)

print "\n-----\n"

if soup.strong != None:
	print "First strong tag:"
	print soup.strong, "\n"

	print "Just the content of the first bolded tag:"
	print soup.strong.string, "\n"

	print "Which element is the parent of this bold one?"
	print soup.strong.parent.name
else:
	print "Hm, no <strong> tags on page. Moving on."


print "\n-----\n"

print "And now all titles on the page:"

headings = soup.findAll('h1')
count = 0

for heading in headings:
	if heading.string != None:
		count += 1
		print str(count) + ") " + str(heading.string)

print "\nThere are a total of %d articles." % count
