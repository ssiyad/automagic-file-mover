from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer

from moover import path

if __name__ == "__main__":
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
