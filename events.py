class EventFileAdded:
    def __init__(self, path):
        self.path = path

class EventFileRemoved:
    def __init__(self, path):
        self.path = path

class EventTaskAdded:
    def __init__(self, process):
        self.process = process

class EventTaskRemoved:
    def __init__(self, process):
        self.process = process