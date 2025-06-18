from concurrent.futures import ThreadPoolExecutor
import queue
import time


def wait_on_future(result_queue):
    f = executor.submit(pow, 5, 2)
    result_queue.put(f)  # Put the Future object in the queue


result_queue = queue.Queue()
with ThreadPoolExecutor(max_workers=1) as executor:
    executor.submit(wait_on_future, result_queue)
    # Retrieve result in the main thread
    future = result_queue.get()
    print(future.result())
