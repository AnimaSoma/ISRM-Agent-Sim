from agent import ISRM_Agent
from stimulus import Stimulus

def run_simulation(steps=2000):
    agent = ISRM_Agent()
    log = []

    for step in range(steps):
        print(f"Step {step} - Energy: {agent.energy:.2f}")
        stim = Stimulus.generate()
        step_log = {"step": step, "energy": agent.energy}

        result = agent.perceive(stim)
        for modality, outcome in result.items():
            val = stim.data[modality]
            print(f"  {modality} ({val:.2f}) -> {outcome}")
            step_log[modality] = {"value": val, "status": outcome}

        log.append(step_log)

    return log

if __name__ == "__main__":
    run_simulation()
