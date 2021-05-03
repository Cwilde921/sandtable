import math
try:
    from StepSequence import StepSequence
except ModuleNotFoundError:
    from .StepSequence import StepSequence

config = {
    "use_steps": StepSequence.FOUR,  # use 4 or 8 step sequence
    "delay_ms": 3,
    
    "pattern_dir": "/home/pi/patterns/",

    "th_motor_pins_wpi": (4,5,6,10),
    "th_motor_pins_bcm": (23,24,25,8),
    "r_motor_pins_wpi": (0,2,3,12),
    "r_motor_pins_bcm": (17,27,22,10),
    
    "gear_ratio_th": 20/289,
    "gear_ratio_r": -20/50,
    "motion": {},
}
    
def calc_motion():
    num_steps = (2048 if config['use_steps'] == StepSequence.FOUR else 4096)
    res = {}
    res['th'] = {}
    res['r'] = {}

    res['th']['th'] = config['gear_ratio_th'] * 2 * math.pi / num_steps
    res['r']['r'] = config['gear_ratio_r'] / num_steps
    res['th']['r'] = res['r']['r'] * config['gear_ratio_th'] # config['gear_ratio_th'] * config['gear_ratio_r']
    res['r']['th'] = 0
    config['motion'] = res 

def change_to_dev_mode():
    config['pattern_dir'] = "../patterns"

calc_motion() 
change_to_dev_mode()
