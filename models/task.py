class Task:
    def __init__(self, title, status="In Progress", assigned_to=None):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def __str__(self):
        return f"Task {self.title} - Status: {self.status}"