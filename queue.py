class Queue:

    def __init__(self):
        self.queue = []

    def themphantu(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False

    def chieudai(self):
        return len(self.queue)

    def bo(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("empty queue")



q1 = Queue()
q1.themphantu("1")
q1.themphantu("2")
q1.themphantu("3")
print(q1.queue)
print("do dai queue:",q1.chieudai())
print("queue sau khi bo:",q1.bo())
print("queue sau khi bo:",q1.bo())