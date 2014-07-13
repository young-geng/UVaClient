import argparse
from login import login, is_logged_in
from result import print_result
from session_store import get_session, write_session
from sys import args, stdout
from getpass import getpass


def do_login():
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


def do_submit():
	parser = argparse.ArgumentParser()
	parser.add_argument("language", type=str, help="programming language", choice=['c', 'c++', 'c++11', 'java', 'pascal'])
	parser.add_argument("problem_ID", type=int, help="problem ID")
	parser.add_argument("file", type=str, help="file to submit")
	args = parser.parse_args()
	





usage = """
usage:
	uva_cli.py <command> [args]

commands:
	login    create a login session for UVa online judge.
	submit 	 submit file to UVa online judge
	list	 list submittion result
"""

commands = {
	"login": 	do_login,
	"submit":	do_submit,
	"list":		do_list
}


def parse_command():
	if len(args) == 0 or args[0] not in commands:
		print usage
		exit(1)
	action = commands[args[0]]
	args = args[1:]
	action()
