"""
Example: How to integrate an LLM (e.g., OpenAI, HuggingFace) into an APC Worker agent.
This shows how a worker can use an LLM to process a ProposeTask.
"""
from apc_core.state_machine import Worker
# import openai  # or from transformers import pipeline

class LLMWorker(Worker):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.llm = openai.ChatCompletion or pipeline(...)

    def execute(self, task):
        prompt = task.params.get('prompt', '')
        # result = self.llm(prompt)  # Call your LLM here
        result = {'output': f"LLM processed: {prompt}"}  # Mocked
        self.state = self.WorkerState.COMPLETED
        self.checkpoint_manager.save_checkpoint(task.base.batch_id, self._serialize_state(), force=True)
        # send Completed (not shown)
        return result

# Usage: Replace Worker with LLMWorker in your agent/server code.
