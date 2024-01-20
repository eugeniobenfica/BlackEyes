import os
import subprocess
import platform
from .events import *

def walk(folder=os.getcwd()):
    result = []

    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)

        if os.path.isdir(item_path):
            result.append(item_path)
            subfolder_content = walk(item_path)
            result.extend(subfolder_content)
        else:
            result.append(item_path)

    return result

def tasks():
    if platform.system() == 'Windows':
        result = subprocess.run(['tasklist'], capture_output=True, text=True)
        processes = result.stdout.split('\n')[3:]
        process_list = [line.split()[0] for line in processes if line.strip()]
        return process_list
    elif platform.system() == 'Linux':
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        processes = result.stdout.split('\n')[1:]
        process_list = [line.split()[10] for line in processes if line.strip()]
        return process_list

class EyeFile:
    def __init__(self, folder: str = os.getcwd()):
        self.folder = folder
        self.folder_items = set(walk(folder))

    def check(self):
        now_folder_items = set(walk(self.folder))
        added = now_folder_items - self.folder_items
        removed = self.folder_items - now_folder_items
        self.folder_items = now_folder_items

        events = []
        for path in added:
            events.append(EventFileAdded(path))
        for path in removed:
            events.append(EventFileRemoved(path))

        return events if events else None

class EyeTask:
    def __init__(self):
        self.tasks = set(tasks())

    def check(self):
        now_tasks = set(tasks())
        added = now_tasks - self.tasks
        removed = self.tasks - now_tasks
        self.tasks = set(tasks())

        events = []
        for task in added:
            events.append(EventTaskAdded(task))
        for task in removed:
            events.append(EventTaskRemoved(task))

        return events if events else None