import os
import glob
import random
from config import config


class Reader:
    # def read_exec_file(self, filename, handler, clear_first=False):
    #     print(filename)
    #     with open(filename, 'r') as f:
    #         for line in f:
    #             handler( read_line_thr(line) )

    @staticmethod
    def get_file_data(filename):
        file_data = {}
        with open(filename, 'r') as f:
            for line in f:
                l = Reader.read_file_data_line(line)
                for key in l:
                    file_data[key] = l[key]
        return file_data

    @staticmethod
    def read_file_data_line(line):
        res = {}
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
                res[line[0]] = line[1]
        return res


    @staticmethod
    def validate_file_name(fname, test_append=True):
        try:
            with open(fname, 'r'):
                pass
            return fname
        except FileNotFoundError:
            if not test_append:
                raise FileNotFoundError
            path = config['pattern_dir']
            if path[-1] == '/':
                path = path[:-1]
            if fname[0] == '/':
                fname = fname[1:]
            if '.' not in fname:
                fname += '.thr'
            elif fname[-4:] != '.thr':
                raise Exception("bad file type")
            return Reader.validate_file_name(path + '/' + fname, test_append=False)

    @staticmethod
    def get_random_file(directory_path=None, subfolder="", extension=".thr"):
        # os.listdir(config["pattern_dir"])
        if directory_path is None:
            directory_path = config['pattern_dir']
        f = random.choice(glob.glob( "{}{}{}*{}".format(directory_path, ('/' if len(subfolder)>0 else ''), subfolder, extension ) ))
        # f = random.choice(glob.glob( directory_path+"*"+extension ))
        return f

    @staticmethod
    def read_line_thr(line:str):
        line = line.strip()
        idx = line.find('#')
        if idx == 0:
            res = Reader.read_file_data_line(line)
            res['is_valid'] = False
            return res
        if idx > 0:
            line = line[:idx]
        line = line.split(' ')
        if len(line) != 2:
            return {'is_valid': False}
            #raise Exception("===== Error found while reading THR line =====\nWrong number of arguments in line. expected {} got {}".format(2, len(line)))
        return {
                'th': float(line[0]),
                'r': float(line[1]),
                'is_valid': True,
            }

    @staticmethod
    def print_cmd(cmd):
        print("th: {}\tr: {}".format(cmd['th'], cmd['r']))

    @staticmethod
    def open_file(fname, validate_file=True):
        if validate_file:
            fname = Reader.validate_file_name(fname)
        with open(fname, 'r') as f:
            for line in f:
                yield line


    class FileQueue:
        def __init__(self):
            self.__queue = []

        def enqueue(self, filename, pos=None, validate=True):
            if validate:
                filename = Reader.validate_file_name(filename)
            if pos is None:
                pos = len(self.__queue)
            self.__queue.insert(pos, filename)

        def pop(self):
            if len(self.__queue) > 0:
                return self.__queue.pop(0)
            else:
                return None

        def peek(self, pos=0):
            if len(self.__queue) > pos:
                return self.__queue[pos]
            else:
                return None

if __name__ == '__main__':
    fname = "sand_table/src/test.txt"
    # fname = "patterns/sandify.thr"
    f = Reader.open_file(fname, validate_file=True)
    print(next(f))
    for i in range(10):
        try:
            print(next(f))
        except StopIteration:
            print("breaking")
            break
    print()
    for cmd in f:
        print(cmd)



