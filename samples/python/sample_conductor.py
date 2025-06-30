"""
Minimal sample Conductor agent using apc-core.
"""
from apc_core.state_machine import Conductor

if __name__ == "__main__":
    conductor = Conductor()
    batch_id = "batch-001"
    steps = ["step1", "step2"]
    conductor.on_new_batch_goal(batch_id, steps)
    print(f"Conductor state: {conductor.state}")
    # Simulate accept and complete
    conductor.on_accept("step1")
    conductor.on_completed("step1")
    print(f"Conductor state: {conductor.state}")
    conductor.on_accept("step2")
    conductor.on_completed("step2")
    print(f"Conductor state: {conductor.state}")
