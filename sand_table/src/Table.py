from Motor import Motor
from Reader import Reader
from config import config
from decimal import *
from time import sleep
import RPi.GPIO as GPIO
import math

class Table:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.__m_th = Motor(config["th_motor_pins_bcm"])
        self.__m_r = Motor(config["r_motor_pins_bcm"])
        self.sleep_time = config['delay_ms'] / 1000
        self.pos = {'th': 0, 'r': 0}
        self.goal = {'th': 0, 'r': 0}
        th_full_steps = math.pi/1024
        self.step_motion_th = config.motion['th'] #{'th': th_full_steps, 'r': (th_full_steps/10)}
        self.step_motion_r = config.motion['r'] #{'th': 0, 'r': (1/2048)}
        #self.reader = Reader()

    def __del__(self):
        del self.__m_th
        del self.__m_r
        GPIO.cleanup()

    #return the distance of new_pos to self.goal
    def heuristic(self, new_pos, version=0):
        if version == 0:
            return (self.goal['r'] ** 2) + (new_pos['r'] ** 2) - ( 2 * self.goal['r'] * new_pos['r'] * math.cos( new_pos['th'] - self.goal['th'] ) )
        if version == 1:
            if(new_pos['r'] >= 1):
                return math.inf
                
            d_r = self.goal['r'] - new_pos['r']
            d_th = self.goal['th'] - new_pos['th']
            return math.sqrt( (d_r * d_r) + (d_th * d_th) )
        if version == 2:
            pass

    # def heuristic(self, new_pos): #P1 = self.pos, P2 = new_pos
    #     return (self.pos['r'] ** 2) + (new_pos['r'] ** 2) - ( 2 * self.pos['r'] * new_pos['r'] * math.cos( new_pos['th'] - self.pos['th'] ) )

    def best_move(self):
        moves = []
        for th in range(-1,2):
            for r in range(-1,2):
                new_pos = self.pos.copy()
                new_pos['th'] += (th * self.step_motion_th['th']) + (r * self.step_motion_r['th'])
                new_pos['r'] += (th * self.step_motion_th['r']) + (r * self.step_motion_r['r'])
                # cost = self.heuristic(new_pos)
                moves.append( {'th':th, 'r':r, 'pos':new_pos, 'cost':self.heuristic(new_pos), 'complete':(th==0 and r==0)} )
        return min(moves, key=lambda x: x['cost'])

    def set_goal(self, goal):
        self.goal['th'] = goal['th']
        self.goal['r'] = goal['r']

    def move(self, move, do_delay=True):
        self.pos['th'] = move['pos']['th']
        self.pos['r'] = move['pos']['r']
        self.__m_th.step(move['th'])
        self.__m_r.step(move['r'])
        if do_delay:
            sleep(self.sleep_time)

    def goto(self, cmd):
        if len(cmd) < 2:
            return
        print(cmd)
        self.set_goal(cmd)
        bm = {'complete': False}
        while not bm['complete']:
            bm = self.best_move()
            self.move(bm)
            #sleep(self.sleep_time)

    #def execute(self, filename):
    #    self.reader.read_exec_file(filename, self.goto)


if __name__ == "__main__":
    t = Table()
    #t.execute("/home/pi/test_patterns/square.thr")
    #t.set_goal({'th': 1, 'r':0.5})
    #t.pos = {'th': 0, 'r':0.9}
    #t.goto({'th': 0, 'r':0.25})
    #sleep(5)
    #for i in range(100):
    #    res = t.best_move()
    #    t.move(res)
    #    print(res)
    #    # print(res['pos']['th'])
    #    # print(res['pos']['r'])
    #    if(res['complete']):
    #        break
    #    print()
    
