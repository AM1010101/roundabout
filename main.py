import threading
import queue

class PubSub:
    def __init__(self):
        self.subscribers = []
        self.q = queue.Queue()

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def unsubscribe(self, callback):
        self.subscribers.remove(callback)

    def publish(self, message):
        self.q.put(message)

    def run(self):
        while True:
            message = self.q.get()
            for subscriber in self.subscribers:
                subscriber(message)

def subscriber1(message):
    print('Subscriber 1 received:', message)

def subscriber2(message):
    print('Subscriber 2 received:', message)

if __name__ == '__main__':
    print('Starting pubsub example...')
    pubsub = PubSub()
    pubsub.subscribe(subscriber1)
    pubsub.subscribe(subscriber2)

    t = threading.Thread(target=pubsub.run)
    t.start()
    while True:
        pubsub.publish('hello world')
        input('Press enter to publish again...')
