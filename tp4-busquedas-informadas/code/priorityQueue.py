# This module increments a priority queue, the higher the priority the closest to the first position of the queue
class PriorityQueueElement:
    value = None
    priority = None

    def __init__(self, value = None, priority = None) -> None:
        if value != None:
            self.set_value(value)
        if priority != None:
            self.set_priority(priority)

    # SETTERS
    def set_value(self, value):
        self.value = value

    def set_priority(self, priority):
        self.priority = priority
    
    # GETTERS
    def get_value(self):
        return self.value

    def get_priority(self):
        return self.priority
    
class PriorityQueue:
    queue = []

    def length(self):
        return len(self.get_queue())

    def enqueue(self, element : PriorityQueueElement):
        queue = self.get_queue()
        elementPriority = element.get_priority()

        if len(queue) == 0: # There are no elements so no priority to compare
            queue.append(element)
        else:
            for i in range(0, len(queue)):
                if elementPriority > queue[i].get_priority():
                    queue.insert(i, element)
                    break

                if i == len(queue) - 1: # This is in case the element we are adding has the smallest priority of all the queue
                    queue.append(element)
    
    def dequeue(self):
        queue = self.get_queue()

        return queue.pop(0)

    def print_queue(self):
        queue = self.get_queue()

        print("[", end= "")
        for i in range(0, len(queue)):
            print("(", queue[i].get_value(), ",", queue[i].get_priority(), ") ; ", end="")
        print("]")

    # SETTERS
    def set_queue(self, queue):
        self.queue = queue

    # GETTERS
    def get_queue(self):
        return self.queue