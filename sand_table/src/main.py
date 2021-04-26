#! /usr/bin/python3

import sys
from shell import loop
from Reader import Reader
from Table import Table
from config import config

args = sys.argv

if '--shell' in args or '-sh' in args:
    loop()
    sys.exit()

file = -1
if '--file' in args:
    file = args.index("--file")
elif '-f' in args:
    file = args.index("-f")

if file >= 0:
    file = config['pattern_dir'] + args[file+1]
    reader = Reader()
    table = Table()
    reader.read_exec_file(file, table.goto)
    sys.exit()
