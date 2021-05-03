class Test:
    def __init__(self):
        self.a = 1

    def __del__(self):
        print("tearing down")

    # def __iter__(self):
    #     return self

    def __next__(self):
        res = self.a
        self.a += 1
        if res >= 4:
            del self
            raise StopIteration
        return res

if __name__ == "__main__":
    t = Test()
    print(next(t))
    print(next(t))
    print(next(t))
    print(next(t))
    # for i in t:
    #     print(i)