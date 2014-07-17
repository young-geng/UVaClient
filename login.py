import requests
from bs4 import BeautifulSoup
from sys import stderr

# dev branch

def is_logged_in(session):
	r = session.get("http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=9")
	return r.text.find("You need to login") == -1

def login(username, password):
	session = requests.Session()
	post_data = {}
	login_page = session.get('http://uva.onlinejudge.org/')
	soup = BeautifulSoup(login_page.text)
	#post hidden data
	try:
		inputs = soup.find('form', attrs={'id': 'mod_loginform'}).find_all('input')
	except Exception:
		print "Sever error!"
		return None
	for i in inputs:
		if i.has_attr('value'):
			post_data[i['name'].encode('ascii','ignore')] = i['value'].encode('ascii','ignore')

	post_data['username'] = username
	post_data['passwd'] = password
	post_data['remember'] = 'yes'

	login_url = 'http://uva.onlinejudge.org/index.php?option=com_comprofiler&task=login'
	r = session.post(login_url, data=post_data)
	#stderr.write(r.text)
	return session

