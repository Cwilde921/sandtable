from Table import Table
from Reader import Reader

def loop():
    table = Table()
    reader = Reader()
    while True:
        inpt = input( "{} {} -> ".format(table.get_pos()['th'], table.get_pos()['r']) )
        if "exit" in inpt:
            break
        elif "set" in inpt:
            if "home" in inpt:
                table.set_pos({'th': 0, 'r':0})
        else:
            inpt = inpt.split('\n')
            for l in inpt:
                try:
                    cmd = reader.read_line_thr(l)
                    table.goto(cmd)
                except:
                    print("\nAn error ocurred. Invalid command")

try:
    loop()
except KeyboardInterrupt:
    print("exiting now")
