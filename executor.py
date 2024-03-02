from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import Optional

class AppExecutor:
    _instance = None

    def __init__(self, max_workers: Optional[int] = None, use_processes: bool = False):
        if use_processes:
            self.executor = ProcessPoolExecutor(max_workers=max_workers)
        else:
            self.executor = ThreadPoolExecutor(max_workers=max_workers)

    @classmethod
    def get_instance(cls, max_workers: Optional[int] = None, use_processes: bool = False):
        if cls._instance is None:
            cls._instance = cls(max_workers, use_processes)
        return cls._instance.executor

    @staticmethod
    def shutdown():
        if AppExecutor._instance:
            AppExecutor._instance.executor.shutdown(wait=True)
