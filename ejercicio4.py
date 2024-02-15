import queue

missions_queue = queue.PriorityQueue()

# Add missions to the queue with their difficulty level
missions_queue.put((3, "Mission 1"))
missions_queue.put((1, "Mission 2"))
missions_queue.put((2, "Mission 3"))
missions_queue.put((4, "Mission 4"))

# Print the missions in order of difficulty
while not missions_queue.empty():
    _, mission = missions_queue.get()
    print(mission)
    