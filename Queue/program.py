from Code.Queue.queue import Queue


if __name__ == "__main__":
    queue = Queue()
    queue.is_empty()
    queue.enque(12)
    queue.enque(17)
    queue.enque(20)
    queue.display()
    queue.peek()
    queue.deque()
    queue.display()
    queue.peek()
    queue.is_empty()
    queue.display()
