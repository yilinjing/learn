import sys, os
from tornado import queues
from tornado import gen
from tornado import ioloop
import tornado

q = queues.Queue(maxsize=2)

def consumer():
    while True:
        item = yield q.get()
        try:
            print('Doing work on %s' % item)
            yield gen.sleep(0.01)
        finally:
            q.task_done()

def producer():
    for item in range(5):
        yield q.put(item)
        print('Put %s' % item)

def main():
    consumer()           # Start consumer.
    yield producer()     # Wait for producer to put all tasks.
    yield q.join()       # Wait for consumer to finish all tasks.
    print('Done')

io_loop = ioloop.IOLoop.current()
io_loop.run_sync(main)
