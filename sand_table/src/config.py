from StepSequence import StepSequence
import math

config = {
    "use_steps": StepSequence.FOUR,  # use 4 or 8 step sequence
    "delay_ms": 3,
    
    "pattern_dir": "/home/pi/patterns/",

    "th_motor_pins_wpi": (4,5,6,10),
    "th_motor_pins_bcm": (23,24,25,8),
    "r_motor_pins_wpi": (0,2,3,12),
    "r_motor_pins_bcm": (17,27,22,10),
    
    "gear_ratio_th": 20/289,
    "gear_ratio_r": 20/100,
    "motion": 
}
    
def calc_motion():
    rad_p_step = math.pi / 1024
    res: {}
    res['th'] = {}
    #
    res['th']['th'] = config['gear_ratio_th'] * rad_p_step
    res['r']['r'] = config['gear_ratio_r'] * rad_p_step
    res['th']['r'] = res['r']['r'] /  #config['gear_ratio_th']
    res['r']['th'] = 0
    
 
