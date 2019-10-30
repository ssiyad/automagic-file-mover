import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from moover import path, LOGGER


class _FileCreatedPrint(FileSystemEventHandler):
    def on_created(self, event):
        LOGGER.info(event)
        print(event.src_path, type(event.src_path))


if __name__ == "__main__":
    LOGGER.info("Moover started in {}".format(path))
    event_handler = _FileCreatedPrint()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
