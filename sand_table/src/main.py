#!/usr/bin/env python3

import sys
from Reader import Reader
from Table import Table
from config import config

def shell_func():
    global table
    # global reader
    try:
        while True:
            inpt = input( "{:.2f} {:.2f} -> ".format(table.get_pos()['th'], table.get_pos()['r']) )
            if "help" in inpt:
                print("\n\n" +\
                    "\t======== Sand Table Shell Help ========\n" +\
                    "exit:                 Exit program.\n" +\
                    "go:\n" +\
                    "    home:             Go to 0, 0.\n" +\
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
            elif "go" in inpt:
                if "home" in inpt:
                    table.go_home()
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
                print(fname)
                try:
                    # Reader.read_exec_file(fname, table.goto)
                    exec_file(fname)
                    
                except KeyboardInterrupt:
                    print("stopping {} early".format(fname))
                except FileNotFoundError:
                    print("{} not found".format(fname))
            
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

def exec_file(fname):
    global table
    f = Reader.open_file(fname, validate_file=True)
    for line in f:
        cmd = Reader.read_line_thr(line)
        if not cmd['is_valid']:
            continue
        table.goto(cmd)


if __name__ == "__main__":
    args = sys.argv

    reader = Reader()
    table = Table()

    if '--help' in args or '-h' in args:
        print("\n" +\
            "================ Help ================\n" +\
            "--help         -h                Show this help\n" +\
            "--go_home      -gh               Run homing sequence\n" +\
            "--shell        -sh               Start sand table shell\n" +\
            "--file         -f   <filename>   Run specified file\n" +\
            "--run          -r                Run random files continuously\n" +\
            "=============== End Help ==============\n" 
        )
        sys.exit()

    if '--go_home' in args or '-gh' in args:
        table.go_home()

    if '--shell' in args or '-sh' in args:
        shell_func()

    file = -1
    if '--file' in args:
        file = args.index("--file")
    elif '-f' in args:
        file = args.index("-f")

    if file >= 0:
        exec_file( args[file] )
        sys.exit()

    if '--run' in args or '-r' in args:
        try:
            while True:
                fname = Reader.get_random_file()
                exec_file(fname)

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
