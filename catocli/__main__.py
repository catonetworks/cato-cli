#!/usr/bin/env python
import sys
import os
from .Utils import clidriver

def main():
	# Check if argcomplete is active (skip usage message if it is)
	if '_ARGCOMPLETE' not in os.environ and sys.argv.__len__() == 1:
		print('Usage: catocli -h')
	else:
		sys.exit(clidriver.main(sys.argv[1:]))

if __name__ == '__main__':
	main()
