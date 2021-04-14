from StepSequence import StepSequence, Dir
from config import config
from typing import Tuple, List
from time import sleep
import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pins:Tuple[int], gpio_setup_teardown=False):
        self.__pins = pins
        self.gpio_setup_teardown = gpio_setup_teardown
        if gpio_setup_teardown:
            GPIO.setmode(GPIO.BCM)
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
        self.__step_seq = StepSequence(config["use_steps"])

    def __del__(self):
        self.release_break()
        #for pin in self.__pins:
        #    GPIO.setup(pin, GPIO.IN)
        if self.gpio_setup_teardown:
            GPIO.cleanup()

    def release_break(self):
        self._write_pins([0,0,0,0])

    def apply_break(self):
        self._write_pins(self.__step_seq.current())

    def step(self, stp:int):
        if   stp ==  0: return self.release_break()
        if   stp ==  1: return self._write_pins(self.__step_seq.next(Dir.CW))
        elif stp == -1: return self._write_pins(self.__step_seq.next(Dir.CCW))
        #self._write_pins(self.__step_seq.next(dir))

    def _write_pins(self, outpt:List[bool]):
        for i in range(len(self.__pins)):
            GPIO.output(self.__pins[i], GPIO.HIGH if outpt[i] else GPIO.LOW)

    def walk(self, steps:int, delay):
        if steps > 0:
            dir = 1
        else:
            dir = -1
            steps = abs(steps)
        for _ in range(steps):
            self.step(dir)
            sleep(delay)
        self.release_break()

if __name__ == "__main__":
    m1 = Motor(config["r_motor_pins_bcm"], True)
    m1.walk(12048, 0.003)
    m1.walk(-12048, 0.003)
    m1.release_break()
