from src.queueclass import Queue

def test_queue_basic():
    q = Queue()
    q.enqueue("a"); q.enqueue("b")
    assert q.dequeue() == "a"
    assert q.peek() == "b"
