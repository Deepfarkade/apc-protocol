"""
Advanced Checkpoint manager for APC.
Supports pluggable backends (in-memory, Redis, S3), checkpoint intervals, and recovery logic.
"""
import threading
import time
import json

class CheckpointBackend:
    def save(self, batch_id, state):
        raise NotImplementedError
    def load(self, batch_id):
        raise NotImplementedError

class InMemoryBackend(CheckpointBackend):
    def __init__(self):
        self._store = {}
    def save(self, batch_id, state):
        self._store[batch_id] = json.dumps(state)
    def load(self, batch_id):
        data = self._store.get(batch_id)
        return json.loads(data) if data else None
    def list_checkpoints(self):
        return list(self._store.keys())

# Placeholders for Redis/S3 backends
class RedisBackend(CheckpointBackend):
    def __init__(self, redis_client):
        self.redis = redis_client
    def save(self, batch_id, state):
        self.redis.set(batch_id, json.dumps(state))
    def load(self, batch_id):
        data = self.redis.get(batch_id)
        return json.loads(data) if data else None

class S3Backend(CheckpointBackend):
    def __init__(self, s3_client, bucket):
        self.s3 = s3_client
        self.bucket = bucket
    def save(self, batch_id, state):
        self.s3.put_object(Bucket=self.bucket, Key=batch_id, Body=json.dumps(state))
    def load(self, batch_id):
        try:
            obj = self.s3.get_object(Bucket=self.bucket, Key=batch_id)
            return json.loads(obj['Body'].read())
        except Exception:
            return None

class CheckpointManager:
    def __init__(self, backend=None, interval=60):
        self.backend = backend or InMemoryBackend()
        self.interval = interval  # seconds
        self._last_checkpoint = {}
        self._lock = threading.Lock()
        self._stop = False
        self._thread = None

    def start_auto_checkpoint(self, batch_id, get_state_fn):
        def run():
            while not self._stop:
                state = get_state_fn()
                self.save_checkpoint(batch_id, state)
                time.sleep(self.interval)
        self._thread = threading.Thread(target=run, daemon=True)
        self._thread.start()

    def stop_auto_checkpoint(self):
        self._stop = True
        if self._thread:
            self._thread.join()
        self._thread = None
        self._stop = False

    def save_checkpoint(self, batch_id, state, force=False):
        """
        Save a checkpoint for a batch. If force=True, bypasses interval check.
        """
        with self._lock:
            now = time.time()
            last = self._last_checkpoint.get(batch_id, 0)
            if force or (now - last >= self.interval):
                self.backend.save(batch_id, state)
                self._last_checkpoint[batch_id] = now

    def load_checkpoint(self, batch_id):
        with self._lock:
            return self.backend.load(batch_id)

    def last_checkpoint_time(self, batch_id):
        with self._lock:
            return self._last_checkpoint.get(batch_id)

    def recover(self, batch_id, recovery_fn, strict=True):
        """
        Loads checkpoint and invokes recovery_fn(state) to resume workflow.
        If strict=True, raises if no checkpoint found.
        """
        state = self.load_checkpoint(batch_id)
        if state:
            recovery_fn(state)
        elif strict:
            raise RuntimeError(f"No checkpoint found for batch {batch_id}")
        return state

    def list_checkpoints(self):
        """
        List all batch_ids with checkpoints (if supported by backend).
        """
        if hasattr(self.backend, 'list_checkpoints'):
            return self.backend.list_checkpoints()
        if isinstance(self.backend, InMemoryBackend):
            return list(self.backend._store.keys())
        return []
