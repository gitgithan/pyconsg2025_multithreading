from concurrent.futures import ThreadPoolExecutor
import concurrent.futures.thread as thread_module
import time


def wait_on_future():
    print("Running wait_on_future")
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())


executor = ThreadPoolExecutor(max_workers=1)
f = executor.submit(wait_on_future)
f.result()  # This will block forever because the worker thread is waiting for itself to finish.
