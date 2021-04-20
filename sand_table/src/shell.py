from Table import Table
from Reader import Reader

def loop():
    table = Table()
    reader = Reader()
    while True:
        inpt = input("->")
        inpt = inpt.split('\n')
        for l in inpt:
            try:
                cmd = reader.read_line_thr(l)
                table.goto(cmd)
            except:
                print("An error ocurred. Invalid command")

try:
    loop()
except KeyboardInterrupt:
    print("exiting now")
