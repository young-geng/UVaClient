UVaClient
=========
Command Line Client for UVa Online Judge


### Dependancy
python 2.7

BeautifulSoup 4.3

requests 2.2


Quick Start
-----------
	python uva_cli.py login

	python uva_cli.py list
	python uva_cli.py list [-l/--limit] "number of submission"

	python uva_cli.py submit "{c, c++, c++11, java, pascal}" "proble ID" "file"


Usage
------
### python uva_cli.py login
Login to UVa online judge to create a session file, session is stored
at "~/.uva_session", and a check sum file is stored at "~/.uva_session_checksum"


### python uva_cli.py list
List your past submission result, and optional number can be added to change the
number of results listed, like "python uva_cli.py list -l 20." The default option
will list 10 latest submissions.


### python uva_cli.py submit "language" "problem ID" "file"
Submit a file to UVa online judge. The language option can be "c", "c++", "c++11",
"java" or "pascal". The problem ID is the ID of problem on UVa website. The file
option is the name of the file going to be submitted.


Tips
-----
1. You can create an alias for uva_cli.py.

	On unix like operating system, you can

		add an alias to your .bashrc or .bash_profile

			alias uva="python <your uva_cli.py path>"

		or create an simbolic link

			ln -s <your uva_cli.py path> ~/bin/lx

	On windows operating system, you can create a bat script uva.bat, and add it to your path

		@echo off
		python <yout uva_cli.py path> %*






