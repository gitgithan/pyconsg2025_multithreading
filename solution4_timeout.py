from concurrent.futures import ThreadPoolExecutor
import concurrent.futures.thread as thread_module
import time


def wait_on_future():
    print("Running wait_on_future")
    f = executor.submit(pow, 5, 2)

    print(f.result())


executor = ThreadPoolExecutor(max_workers=1)
f = executor.submit(wait_on_future)
f.result(timeout=1)
