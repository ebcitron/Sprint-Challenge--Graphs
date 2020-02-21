
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def traverse(room_graph):
    #Create an empty stack for our path
    path = Stack()
    path.push(0)
    #Create an array of our guided path
    dir_guide = []
    #empty set to store visited nodes
    visited = set()

#Continue while theres still rooms to visit
    while len(visited) <len(room_graph):
        #Get the id from the current room and set it in visited
        id = path.stack[-1]
        visited.add(id)

        inRoom = room_graph[id]

        #map out adjacant rooms

        adjacent = inRoom[1]

        #keep track of any new rooms

        newRooms = []

        #If adjacent, append to newRooms array

        for direction, adjId in adjacent.items():
            if adjId not in visited:
                newRooms.append(adjId)
        #As long as the length of newRooms is not 0, we move forward, else we reverse back and 

        if len(newRooms)> 0:
            nextUp = newRooms[0]
            path.push(nextUp)
            #else continue

        else:
            path.pop()
            nextUp = path.stack[-1]

        for direction, adjId in adjacent.items():
            if adjId == nextUp:
                dir_guide.append(direction)
    return dir_guide



