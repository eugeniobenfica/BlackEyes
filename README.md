# BlackEyes

A library designed for vigilant observation and tracking of file system changes and running processes. BlackEyes empowers you with the ability to monitor alterations in files and tasks within a specified folder, providing valuable insights into the dynamics of your system.

## Key Features

- **File System Tracking:** Keep a keen eye on added and removed files within a designated folder.
- **Task Monitoring:** Stay informed about newly initiated and terminated processes on your system.
- **Cross-Platform Compatibility:** BlackEyes supports both Windows and Linux environments seamlessly.
- **User-Friendly API:** Easily integrate BlackEyes into your Python projects using the intuitive API.

## Installation

1. Download the BlackEyes library [here](https://github.com/eugeniobenfica/BlackEyes/releases/download/1.0.0/blackeyes.zip).
2. Integrate BlackEyes into your Python environment using the following Labyrinth command:

```bash
python labrt.py add blackeyes.zip
```

## Usage

```python
from blackeyes import EyeFile, EyeTask

# Initialize file monitoring for a specific folder
file_monitor = EyeFile(folder="/path/to/target/folder")

# Initialize task monitoring
task_monitor = EyeTask()

# Check for file system changes
file_events = file_monitor.check()

# Check for task-related events
task_events = task_monitor.check()

# Process and respond to events as needed
if file_events:
    for event in file_events:
        print(f"File Event: {event}")
        
if task_events:
    for event in task_events:
        print(f"Task Event: {event}")
```

Enhance your system awareness with BlackEyes. Detect changes, track tasks, and keep your finger on the pulse of your environment.

*Monitor. Detect. Empower with BlackEyes.*
