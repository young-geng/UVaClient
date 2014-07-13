from bs4 import BeautifulSoup
from session_store import write_session
import requests
import re
from sys import stdout
import locale
locale.setlocale(locale.LC_NUMERIC, "")


def parse_result(page_text):
	result = []
	try:
		soup = BeautifulSoup(page_text)
		for entry in soup.find('div', attrs={'id': 'col3_content_wrapper'})\
						 .find('table')\
						 .find_all('tr', attrs={'class': re.compile(r'sectiontableentry[0-9]*')}):
			row = []
			for e in entry.find_all('td'):
				row.append(e.get_text())
			result.append(row)
	except Exception:
		return []
	return result


def get_max_width(table, index):
	return max([len(str(row[index])) for row in table])

def pprint_table(out, table):
	col_paddings = []
	for i in range(len(table[0])):
		col_paddings.append(get_max_width(table, i))

	for row in table:
		print >> out, row[0].ljust(col_paddings[0] + 1),
		for i in range(1, len(row)):
			col = str(row[i]).rjust(col_paddings[i] + 2)
			print >> out, col,
		print >> out


def print_result_table(result_table):
	table_head = ['#', 'Problem', 'Name', 'Verdict', 'Language', 'Run Time', 'Date']
	result_table.insert(0, table_head)
	pprint_table(stdout, result_table)


def get_result_page(session, limit):
	assert type(limit) == int and limit >= 1
	url = """http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=9&limit={0}&limitstart=0""".format(limit)
	try:
		page = session.get(url).text
	except requests.exceptions.ConnectionError:
		print "Connection error, please try again later"
		write_session(session)
		exit(1)
	return page


def print_result(session, limit):
	print_result_table(parse_result(get_result_page(session, limit)))
