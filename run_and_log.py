import os
import time
from main import run_simulation  # This assumes your main.py has a run_simulation() function

# Ensure log directory exists
log_dir = "simulation_logs"
os.makedirs(log_dir, exist_ok=True)

# Generate a timestamped filename
timestamp = time.strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f"run_{timestamp}.txt")

# Redirect stdout to the log file
with open(log_file, "w") as f:
    original_stdout = os.sys.stdout
    os.sys.stdout = f

    try:
        run_simulation()
    finally:
        os.sys.stdout = original_stdout

print(f"✅ Simulation complete. Output saved to: {log_file}")
