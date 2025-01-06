import queue

class TaskQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def add_task(self, task):
        """
        Add a task to the queue after validating it.
        """
        if not task.get("action") or not task.get("target"):
            print("Error: Task must include both 'action' and 'target'.")
            return
        self.queue.put(task)
        print(f"Task added: {task}")

    def process_task(self):
        """
        Process the next task in the queue.
        """
        if not self.queue.empty():
            task = self.queue.get()
            if callable(task):
                task()  # If task is callable, execute it
            else:
                print(f"Executing task: {task}")  # Otherwise, print the task
            return task
        else:
            print("No tasks in the queue.")
            return None

    def cancel_task(self, task):
        """
        Remove a task from the queue if it exists.
        """
        tasks = list(self.queue.queue)  # Convert to a list for easier manipulation
        if task in tasks:
            tasks.remove(task)
            self.queue = queue.Queue()
            for remaining_task in tasks:
                self.queue.put(remaining_task)
            print(f"Task cancelled: {task}")
        else:
            print(f"Task not found: {task}")
