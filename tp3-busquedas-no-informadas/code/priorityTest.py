import priorityQueue

queue = priorityQueue.PriorityQueue()
element1 = priorityQueue.PriorityQueueElement("element1", 1)
element2 = priorityQueue.PriorityQueueElement("element2", 2)
element3 = priorityQueue.PriorityQueueElement("element3", 3)
element4 = priorityQueue.PriorityQueueElement("element4", 4)
element5 = priorityQueue.PriorityQueueElement("element5", 5)
element6 = priorityQueue.PriorityQueueElement("element6", 6)

queue.enqueue(element5)
queue.enqueue(element2)
queue.enqueue(element1)
queue.enqueue(element6)
queue.enqueue(element4)
queue.enqueue(element3)

queue.print_queue()
print(queue.length())

print(queue.dequeue().get_value())

queue.print_queue()

queue.dequeue()

queue.print_queue()