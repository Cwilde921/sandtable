#!/usr/bin/env python3

import sys
from Reader import Reader
from Table import Table
from config import config

args = sys.argv

reader = Reader()
table = Table()

if '--shell' in args or '-sh' in args:
    try:
        while True:
            inpt = input( "{:.2f} {:.2f} -> ".format(table.get_pos()['th'], table.get_pos()['r']) )
            if "help" in inpt:
                print("\n\n" +\
                    "\t======== Sand Table Shell Help ========\n" +\
                    "exit:                 Exit program.\n" +\
                    "set:\n" +\
                    "    home:             Set current position to 0, 0.\n" +\
                    "    safe:             Set to safe mode.\n" +\
                    "    dangerous:        Set to unprotected mode.\n" +\
                    "file:\n" +\
                    "    <filename>:       Fun file from patterns directory.\n" +\
                    "<theta> <rho>:        Goto position specified.\n" +\
                    "\t=============== End Help ==============\n\n" 
                )

            if "exit" in inpt:
                break
            elif "set" in inpt:
                if "home" in inpt:
                    table.set_pos({'th': 0, 'r':0})
                if "safe" in inpt:
                    table.set_safe(True)
                if "dangerous" in inpt:
                    table.set_safe(False)
            elif "file" in inpt:
                args = inpt.split(' ')
                fname = args[args.index("file")+1]
                path = config['pattern_dir']
                if(path[-1] != '/'): path = path + '/'
                fname = path + fname
            
            else:
                inpt = inpt.split('\n')
                for l in inpt:
                    try:
                        cmd = reader.read_line_thr(l)
                        table.goto(cmd)
                    except:
                        print("\nAn error ocurred. Invalid command")
    except KeyboardInterrupt:
        print("\nGoodbye")
    sys.exit()

file = -1
if '--file' in args:
    file = args.index("--file")
elif '-f' in args:
    file = args.index("-f")

if file >= 0:
    path = config['pattern_dir']
    if(path[-1] != '/'): path = path + '/'
    fname = path + args[file+1]
    reader.read_exec_file(fname, table.goto)
    sys.exit()

if '--help' in args or '-h' in args:
    print("\n" +\
        "================ Help ================\n" +\
        "--help:   -h:               Show this help\n" +\
        "--shell:  -sh:              Start sand table shell\n" +\
        "--file:   -f:   <filename>  Run specified file\n" +\
        "--run:    -r:               Run random files continuously\n" +\
        "=============== End Help ==============\n" 
    )
    sys.exit()

if '--run' in args or '-r' in args:
    try:
        reader.run(table.goto)
    except KeyboardInterrupt:
        print("\nGoodbye")
    sys.exit()

# def loop(table, reader):
#     while True:
#         inpt = input( "{%.2f} {%.2f} -> ".format(table.get_pos()['th'], table.get_pos()['r']) )
#         if "exit" in inpt:
#             break
#         elif "set" in inpt:
#             if "home" in inpt:
#                 table.set_pos({'th': 0, 'r':0})
#         elif "file" in inpt:
#             args = inpt.split(' ')
#             fname = args[args.index("file")+1]
#             path = config['pattern_dir']
#             if(path[-1] != '/'): path = path + '/'
#             fname = path + fname
        
#         else:
#             inpt = inpt.split('\n')
#             for l in inpt:
#                 try:
#                     cmd = reader.read_line_thr(l)
#                     table.goto(cmd)
#                 except:
#                     print("\nAn error ocurred. Invalid command")
