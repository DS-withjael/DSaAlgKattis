

class Flight:
    def __init__(self, time, destination):
        self.time = time
        self.destination = destination

    def info(self):
        print("Departure time is", self.time, "going to", self.destination)




flights , ops = map(int, input().split())

