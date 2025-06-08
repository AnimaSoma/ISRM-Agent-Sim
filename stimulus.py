import random

class Stimulus:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def generate():
        return Stimulus({
            "light": random.uniform(0, 10),
            "sound": random.uniform(0, 10),
            "touch": random.uniform(0, 10),
            "temperature": random.uniform(0, 10)
        })
