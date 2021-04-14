from StepSequence import StepSequence

config = {
    "use_steps": StepSequence.FOUR,  # use 4 or 8 step sequence
    "pattern_dir": "/home/pi/patterns/",

    "th_motor_pins_wpi": (4,5,6,10),
    "th_motor_pins_bcm": (23,24,25,8),
    "r_motor_pins_wpi": (0,2,3,12),
    "r_motor_pins_bcm": (17,27,22,10),

    "delay_ms": 3,
}
