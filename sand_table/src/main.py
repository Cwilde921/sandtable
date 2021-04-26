import sys

args = sys.args

file = -1
if '--file' in args:
    file = args.index("--file")
elif '-f' in args:
    file = args.index("-f")

file = None if file < 0 else args[file+1]


