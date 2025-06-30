"""
State machine logic for APC Conductor and Worker roles.
"""
from enum import Enum, auto
from apc_core.checkpoint import CheckpointManager
from apc_core.messages import apc_pb2

class ConductorState(Enum):
    IDLE = auto()
    PROPOSING = auto()
    SEQUENCING = auto()
    COMPLETED = auto()

class WorkerState(Enum):
    IDLE = auto()
    EXECUTING = auto()
    COMPLETED = auto()
    FAILED = auto()

class Conductor:
    def __init__(self, checkpoint_manager=None):
        self.state = ConductorState.IDLE
        self.current_step = None
        self.batch_id = None
        self.history = []
        self.checkpoint_manager = checkpoint_manager or CheckpointManager()

    def on_new_batch_goal(self, batch_id, steps):
        self.state = ConductorState.PROPOSING
        self.batch_id = batch_id
        self.steps = steps
        self.current_step = 0
        self.checkpoint_manager.save_checkpoint(batch_id, self._serialize_state(), force=True)
        # send ProposeTask for first step

    def on_accept(self, step_name):
        self.state = ConductorState.SEQUENCING
        self.checkpoint_manager.save_checkpoint(self.batch_id, self._serialize_state())
        # ...

    def on_completed(self, step_name):
        self.history.append(step_name)
        if self.current_step + 1 < len(self.steps):
            self.current_step += 1
            self.checkpoint_manager.save_checkpoint(self.batch_id, self._serialize_state())
            # send next ProposeTask
        else:
            self.state = ConductorState.COMPLETED
            self.checkpoint_manager.save_checkpoint(self.batch_id, self._serialize_state(), force=True)

    def on_failed(self, step_name):
        # pick alternate worker or send TakeOver
        self.checkpoint_manager.save_checkpoint(self.batch_id, self._serialize_state(), force=True)
        pass

    def _serialize_state(self):
        return {
            'state': self.state.name,
            'current_step': self.current_step,
            'batch_id': self.batch_id,
            'history': self.history,
            'steps': self.steps if hasattr(self, 'steps') else []
        }

    def recover_from_checkpoint(self):
        state = self.checkpoint_manager.load_checkpoint(self.batch_id)
        if state:
            self.state = ConductorState[state['state']]
            self.current_step = state['current_step']
            self.batch_id = state['batch_id']
            self.history = state['history']
            self.steps = state['steps']

class Worker:
    def __init__(self, checkpoint_manager=None):
        self.state = WorkerState.IDLE
        self.checkpoint_manager = checkpoint_manager or CheckpointManager()

    def on_propose_task(self, task):
        if self.can_handle(task):
            self.state = WorkerState.EXECUTING
            self.checkpoint_manager.save_checkpoint(task.batch_id, self._serialize_state())
            # send Accept
        else:
            # send Reject
            pass

    def can_handle(self, task):
        # Implement capability check
        return True

    def execute(self, task):
        try:
            # ... do work ...
            self.state = WorkerState.COMPLETED
            self.checkpoint_manager.save_checkpoint(task.batch_id, self._serialize_state(), force=True)
            # send Completed
        except Exception as e:
            self.state = WorkerState.FAILED
            self.checkpoint_manager.save_checkpoint(task.batch_id, self._serialize_state(), force=True)
            # send Failed

    def _serialize_state(self):
        return {
            'state': self.state.name
        }

    def recover_from_checkpoint(self, batch_id):
        state = self.checkpoint_manager.load_checkpoint(batch_id)
        if state:
            self.state = WorkerState[state['state']]
