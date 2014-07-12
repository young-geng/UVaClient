import pickle
import requests
from hashlib import md5

session_file_name = "~/.uva_session_checksum"
session_checksum_name = "~/.uva_session"


def exist_session_file():
	try:
		open(session_file_name)
		open(session_checksum_name)
	except Exception:
		return False
	return True


def is_valid_session_file():
	session_file = open(session_file_name).read()
	hash_code = open(session_checksum_name).read()
	return md5(session_file).hexdigest() == md5(session_file).hexdigest()

def get_session():
	if not exist_session_file():
		return None
	elif not is_valid_session_file():
		return None
	return pickle.load(open(session_file_name))

def write_session(session):
	pickle.dump(session, open(session_file_name, 'w'))
	open(session_checksum_name, 'w').write(md5(open(session_file_name).read()).hexdigest())


if __name__ == '__main__':
	x = [1, 2, 'abc']
	session_file_name = "temp1"
	session_checksum_name = "temp2"
	write_session(x)
	print exist_session_file()
	print is_valid_session_file()
	print get_session()