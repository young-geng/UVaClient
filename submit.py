import requests
from sys import stderr
import re


def submit(session, problem_id, language, source):
	language_code = {
		'c':		1,
		'java':		2,
		'c++':		3,
		'pascal':	4,
		'c++11':	5
	}
	url = "http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25&page=save_submission"
	data = {
		'problemid':	'',
		'category':		'',
		'localid':		problem_id,
		'language':		language_code[language],
		'code':			source
	}
	session.post(url, data=data)

