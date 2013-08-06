
# Another BeautifulSoup test
# This one prints the first 10 links on a page and counts the total

# To make parts of it reusable in other scripts, I used functions

from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError
import re


def ask_for_url():
    user_url = raw_input('Which page do you want to check?\n')

    while not(re.match(r'https?://', user_url)):
    	user_url = raw_input('Type in a link beginning with http://\n')

    return user_url

# just checking if the url is working
# code borrowed from http://stackoverflow.com/questions/11983049/python-read-and-validate-input-url
def check_url(user_url):
    page_url = "http://blog.ialja.com"

    req = Request(user_url)
    try:
        response = urlopen(req)
    except URLError, e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            #print 'Reason: ', e.reason
            print "I'll just give you an example with %s" % page_url
            #page_content = urlopen(page_url)
        elif hasattr(e, 'code'):
            print 'Sorry, couldn\'t reach that server.'
            #print 'Error code: ', e.code
            print "I'll just give you an example with %s" % page_url
            #page_content = urlopen(page_url)
    else:
        #page_content = response
        page_url = user_url
    return page_url

def find_links(page_url):
    page_content = urlopen(page_url)
    soup = BeautifulSoup(page_content)

    links = soup.findAll('a')
    count = 0

    print "\n-----\n"
    print "LISTING FIRST 10 LINKS FOR PAGE:"
    print page_url
    print "-----\n"

    for link in links:
        link_url = link.get('href')
        if link_url != None and link_url != "/" and not(link_url.startswith("#")):
            if count < 10:
                print link_url
            count += 1

    print "\nThere are a total of %d links." % count

    print "\n-----\n"

    return count

find_links(check_url(ask_for_url()))
