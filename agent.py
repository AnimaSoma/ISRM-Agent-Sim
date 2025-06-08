from metabolism import MetabolicState

class ISRM_Agent:
    def __init__(self):
        self.energy = 100.0
        self.memory = {}
        self.metabolism = MetabolicState()

    def perceive(self, stimuli):
        self.metabolism.update(0)
        energy_modifier = self.metabolism.get_energy_modifier()

        total_energy_used = 0.0
        actions = {}

        # Fix: explicitly handle Stimulus wrapper
        if hasattr(stimuli, "data") and isinstance(stimuli.data, dict):
            stimuli = stimuli.data
        elif not isinstance(stimuli, dict):
            raise TypeError("Stimuli must be a dict or an object with a .data dict.")

        for modality, value in stimuli.items():
            prediction = self.memory.get(modality, None)
            if prediction is None or abs(prediction - value) > 2.0:
                cost = 1.0 * energy_modifier
                total_energy_used += cost
                self.memory[modality] = value
                actions[modality] = 'updated'
            else:
                actions[modality] = 'ignored'

        self.energy = max(0, self.energy - total_energy_used)
        return actions
