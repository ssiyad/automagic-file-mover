import os
import shutil
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from moover import SOURCE, DESTINATION, LOGGER


class _FileCreatedPrint(FileSystemEventHandler):
    def on_created(self, event):
        if os.path.isdir(event.src_path):
            LOGGER.info("Directory created: {}".format(event.src_path))
        else:
            LOGGER.info("File created: {}".format(event.src_path))
            extension = os.path.splitext(event.src_path)[-1]
            ext_sub_dir = os.path.join(DESTINATION, extension.upper()[1:])
            if not _DirFunctions(ext_sub_dir).check_dir():
                _DirFunctions(ext_sub_dir).make_dir()
                LOGGER.info("Created new category: {}".format(ext_sub_dir))
            shutil.move(event.src_path, ext_sub_dir)
            LOGGER.info("Moved~ {} to {}".format(event.src_path, ext_sub_dir))


class _DirFunctions(object):
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def check_dir(self):
        if os.path.exists(self.dir_path):
            return True
        else:
            return False

    def make_dir(self):
        try:
            os.mkdir(self.dir_path)
        except Exception:
            raise Exception


if __name__ == "__main__":
    if not _DirFunctions(SOURCE).check_dir():
        _DirFunctions(SOURCE).make_dir()
        LOGGER.info("CREATED SOURCE DIRECTORY: {}".format(SOURCE))
    if not _DirFunctions(DESTINATION).check_dir():
        _DirFunctions(DESTINATION).make_dir()
        LOGGER.info("CREATED DESTINATION DIRECTORY: {}".format(DESTINATION))
    LOGGER.info("Moover started in {} -> {}".format(SOURCE, DESTINATION))
    list_dir = [name for name in os.listdir(DESTINATION)
                if os.path.isdir(os.path.join(DESTINATION, name))]

    if len(list_dir) < 1:
        sub_dirs = "No Sub-Directories are present in {}".format(DESTINATION)
    else:
        sub_dirs = "Sub-Directories present in {}: {}".format(DESTINATION, " | ".join([name for name in list_dir]))

    LOGGER.info(sub_dirs)
    event_handler = _FileCreatedPrint()
    observer = Observer()
    observer.schedule(event_handler, SOURCE, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
