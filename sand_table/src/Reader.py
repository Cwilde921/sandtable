import os
import glob
import random
from config import config

class Reader:
    def __init__(self):
        self.__queue = []
        self.file_data = {}

    def enqueue_back(self, filename):
        self.__queue.append(filename)

    def enqueue_front(self, filename):
        self.__queue.insert(0, filename)

    def _dequeue(self):
        if len(self.__queue) > 0:
            return self.__queue.pop(0)
        else:
            return random.choice(glob.glob(config['pattern_dir']+"*.thr"))

    def get_random_file(self):
        # os.listdir(config["pattern_dir"])
        f = random.choice(glob.glob(config['pattern_dir']+"*.thr"))
        return f

    def run(self, table, do_home=False):
        while True:
            f = self._dequeue()
            self.file_data = {}
            self.get_file_data(f)
            #if 'Start Point' in self.file_data:
            #    if self.file_data['Start Point'] == 'center':
            #        self.read_exec_file(config['pattern_dir']+'clear/center.thr', handler, clear_first=False)
            #    else:
            #        self.read_exec_file(config['pattern_dir']+'clear/perimeter.thr', handler, clear_first=False)
            if do_home:
                table.go_home()
            self.read_exec_file(f, table.goto, clear_first=True)
            

    def read_exec_file(self, filename, handler, clear_first=False):
        print(filename)
        with open(filename, 'r') as f:
            for line in f:
                handler( self.read_line_thr(line) )

    def get_file_data(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                idx = line.find('#')
                if idx == 0:
                    line = line[1:]
                    line = line.strip()
                    if ':' in line:
                        line = line.split(':')
                        for i in range(len(line)):
                            line[i] = line[i].strip()
                        if len(line) == 2:
                            try: 
                                line[1] = float(line[1])
                            except ValueError:
                                pass
                        self.file_data[line[0]] = line[1]

                

    def read_line_thr(self, line:str, get_data=False):
        line = line.strip()
        idx = line.find('#')
        if idx == 0:
            #if get_data:
            #    line = line[1:]
            #    line = line.strip()
            #    if ':' in line:
            #        line = line.split(':')
            #        for i in range(len(line)):
            #            line[i] = line[i].strip()
            #        if len(line) == 2:
            #            try: 
            #                line[1] = float(line[1])
            #            except ValueError:
            #                pass
            #        self.file_data[line[0]] = line[1]
            return {}

        if idx > 0:
            line = line[:idx]
        line = line.split(' ')
        if len(line) < 2:
            return {}
        if len(line) != 2:
            return {}
            #raise Exception("===== Error found while reading THR line =====\nWrong number of arguments in line. expected {} got {}".format(2, len(line)))
        return {
                'th': float(line[0]),
                'r': float(line[1]),
            }

    def print_cmd(self, cmd):
        print("th: {}\tr: {}".format(cmd['th'], cmd['r']))

if __name__ == '__main__':
    def func(cmd):
        if len(cmd) == 0:
            return
        r = Reader()
        r.print_cmd(cmd)


    # Reader.read_exec_file("../test_patterns/sandify.thr", func)
    r = Reader()
    r.read_exec_file("../test_patterns/sandify(5).thr", func)
    print(r.file_data)
    # print(r.get_random_file())



