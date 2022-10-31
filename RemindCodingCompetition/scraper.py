# importing all the necessary libraries
import requests
from dateutil.parser import parse
#importing beautiful soup after installing it
from bs4 import BeautifulSoup

#defining the choice of contest platform. Here in this case im using codechef
def codechef():
    url = "https://www.codechef.com/contests"
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    arr = []
    table = soup.find_all('table', {"class":"dataTable"})[1].tbody.findAll('tr')

    for item in table:
        obj = {}
        tds = item.findAll('td')
        obj['link'] = 'https://www.codechef.com' + tds[1].contents[0]['href']
        obj['name'] = tds[1].contents[0].text
        obj['startTime'] = parse(tds[2]['data-starttime'])
        obj['endTime'] = parse(tds[3]['data-endtime'])
        obj['platform'] = 'codechef'
        arr.append(obj)

    return arr

    
def process():
    #Scraping Codechef
    tempContests = codechef.codechef()
    contests = contests+ tempContests

    return contests