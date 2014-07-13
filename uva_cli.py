import argparse
from login import login, is_logged_in
from submit import submit
from result import print_result
from session_store import get_session, write_session
from sys import stdout, stdin
from getpass import getpass


def do_login(args):
	stdout.write("Username: ")
	username = stdin.readline().strip()
	password = getpass()
	session = login(username, password)
	if is_logged_in(session):
		print "Logged in successfully!"
		write_session(session)
	else:
		print "Login failed!"
		exit(1)


def do_submit(args):
	try:
		src = open(args.file).read()
	except Exception:
		print "File not found!"
		exit(1)
	session = get_session()
	if session == None or not is_logged_in(session):
		print "Invalid session. Please login."
		exit(1)
	if args.problem_ID < 1:
		print "Invalid problem ID!"
		exit(1)
	submit(session, args.problem_ID, args.language, src)
	print "File submitted!"

def do_list(args):
	session = get_session()
	if session == None or not is_logged_in(session):
		print "Invalid session. Please login."
		exit(1)
	if args.limit < 1:
		print "Invalid limit number!"
		exit(1)
	print_result(session, args.limit)


	

if __name__ == "__main__":

	parser = argparse.ArgumentParser(prog='uva_cli.py')
	subparsers = parser.add_subparsers(dest='command')

	login_parser = subparsers.add_parser('login', help='Login to UVa Online Judge')


	submit_parser = subparsers.add_parser('submit', help='submit a file to UVa OJ')
	submit_parser.add_argument('language', type=str, choices=['c', 'c++', 'c++11', 'java', 'pascal'], help='programming language')
	submit_parser.add_argument('problem_ID', type=int, help='problem ID')
	submit_parser.add_argument('file', type=str, help='source file')

	list_parser = subparsers.add_parser('list', help='list submission result')
	list_parser.add_argument('-l', '--limit', type=int, help='max number of results', default=5)

	args = parser.parse_args()

	commands = {
		"login": 	do_login,
		"submit":	do_submit,
		"list":		do_list
	}

	commands[args.command](args)

