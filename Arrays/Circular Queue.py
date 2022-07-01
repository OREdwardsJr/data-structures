class CircularQueue:
    def __init__(self, n):
        self.q = [None] * n
        self.front = -1
        self.rear = -1
        self.n = n

    def enqueue(self, val):
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.q[self.rear] = val
        elif (self.rear + 1) % self.n == self.front:
            print(-1)
        else:
            self.rear = (self.rear + 1) % self.n
            self.q[self.rear] = val

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print(-1)
        elif self.front == self.rear:  # only one element left
            self.front = self.rear = -1  # reset queue
        else:
            self.front = (self.front + 1) % self.n

    def peek(self):
        print(self.q[self.front])

    def display(self):
        if self.front == self.rear == -1:
            print([] * self.n)
        else:
            i = self.front
            j = self.rear
            while i % self.n != j:
                print(self.q[i])
                i = (i + 1) % self.n

            print(
                self.q[i]
            )  # This is positioned here to prevent infinite loop due to use of mod(%)


q = CircularQueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.enqueue(6)
q.display()
