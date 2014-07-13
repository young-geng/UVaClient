import pickle
import requests
from hashlib import md5
import os

user_home = os.getenv('USERPROFILE') or os.getenv('HOME')
session_file_name = os.path.join(user_home, ".uva_session")
session_checksum_name = os.path.join(user_home, ".uva_session_checksum")


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
	try:
		pickle.dump(session, open(session_file_name, 'w'))
		open(session_checksum_name, 'w').write(md5(open(session_file_name).read()).hexdigest())
	except:
		print "Saving session failed!\n Check if you have permission to access \"{0}\" and \"{1}\"".format(session_file_name, session_checksum_name)
		exit(1)

