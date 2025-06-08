# metabolism.py

class MetabolicState:
    def __init__(self):
        self.glucose = 100.0        # in arbitrary units
        self.serotonin = 1.0        # 1.0 = full; 0.0 = depleted
        self.dopamine = 1.0
        self.time_of_day = 0        # 0–23 hour representation
        self.circadian_modifier = 1.0

    def update(self, step):
        # Simulate circadian rhythm (less efficient energy usage at night)
        self.time_of_day = (self.time_of_day + 1) % 24
        if 0 <= self.time_of_day < 6 or 20 <= self.time_of_day < 24:
            self.circadian_modifier = 0.8  # Reduced metabolism
        else:
            self.circadian_modifier = 1.0

        # Simulate gradual depletion
        self.glucose = max(self.glucose - 0.5, 0)
        self.serotonin = max(self.serotonin - 0.01, 0)
        self.dopamine = max(self.dopamine - 0.005, 0)

    def replenish(self, glucose=10.0, serotonin=0.05, dopamine=0.02):
        self.glucose = min(self.glucose + glucose, 100.0)
        self.serotonin = min(self.serotonin + serotonin, 1.0)
        self.dopamine = min(self.dopamine + dopamine, 1.0)

    def get_energy_modifier(self):
        # Lower serotonin or glucose makes processing costlier
        base_modifier = 1.0
        if self.glucose < 20:
            base_modifier += 0.5
        if self.serotonin < 0.3:
            base_modifier += 0.3
        return base_modifier * self.circadian_modifier
