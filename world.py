# world.py

import random
from stimulus import Stimulus

def generate_stimuli():
    stimuli = []
    for name in ["light", "sound", "touch", "temperature"]:
        value = random.uniform(0, 10)
        stimuli.append(Stimulus(name, value))
    return stimuli
