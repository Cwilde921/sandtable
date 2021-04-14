from enum import Enum

class Dir(Enum):
    CW = True
    CCW = False


class StepSequence:
    # class Seq(Enum):
    FOUR = 4
    EIGHT = 8

    def __init__(self, step_seq:int):
        self.steps = [
                [1, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1],
            ]
        self.step_seq = step_seq
        self._step_ctr = 0

    def next(self, dir:Dir):
        self._update_ctr(dir)
        return self.steps[self._step_ctr]

    def current(self):
        return self.steps[self._step_ctr]

    def _update_ctr(self, dir:Dir):
        stp = 1 if self.step_seq == self.EIGHT else 2
        if(dir == Dir.CW):
            self._step_ctr += stp
            if(self._step_ctr >= len(self.steps)):
                self._step_ctr = 0
        else:
            self._step_ctr -= stp
            if(self._step_ctr < 0):
                self._step_ctr = len(self.steps) -stp


if __name__ == "__main__":

    ss = StepSequence(StepSequence.FOUR)
    for i in range(20):
        print(ss.next(Dir.CW))
    print("changing direction")
    for i in range(15):
        print(ss.next(Dir.CCW))