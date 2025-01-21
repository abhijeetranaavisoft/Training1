class AssignmentQueue:
    def __init__(self):
        self.queue = []  

    def enqueue(self, assignment):
        self.queue.append(assignment)
        print(f"Assignment '{assignment}' added to the queue.")

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return 

    def dequeue(self):
        if not self.isEmpty():
            completed_assignment = self.queue.pop(0)
            print(f"Assignment '{completed_assignment}' completed and removed from the queue.")
        else:
            print("No assignments to remove. The queue is empty.")

    def isEmpty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

if __name__ == "__main__":
    sindhu_queue = AssignmentQueue()

    sindhu_queue.enqueue("Math Homework")
    sindhu_queue.enqueue("Science Project")
    sindhu_queue.enqueue("History Essay")

    print("Oldest assignment:", sindhu_queue.peek())

    sindhu_queue.dequeue()
    sindhu_queue.dequeue()

    print("Oldest assignment:", sindhu_queue.peek())
    
    print("Is the queue empty?", sindhu_queue.isEmpty())

    sindhu_queue.dequeue()

    print("Is the queue empty?", sindhu_queue.isEmpty())
