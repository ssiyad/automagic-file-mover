import logging

from pathlib import Path

import sys
import os


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

DEFAULT = {"SOURCE_DIR": "Downloads", "DESTINATION_DIR": "Moover"}

LOGGER = logging.getLogger(__name__)

if len(sys.argv) != 3:
    if len(sys.argv) > 3:
        LOGGER.error("Syntax: moover <source_dir> <dest_dir>")
        exit(0)
    elif len(sys.argv) == 2:
        LOGGER.warn("Setting DESTINATION as {}".format(1))
        SOURCE = os.path.join(Path.home(), DEFAULT["SOURCE_DIR"])
        DESTINATION = os.path.join(Path.home(), sys.argv[1])
    else:
        LOGGER.warn("Using Default SOURCE:MooverTestDir and DESTINATION:Moover")
        SOURCE = os.path.join(Path.home(), DEFAULT["SOURCE_DIR"])
        DESTINATION = os.path.join(Path.home(), DEFAULT["DESTINATION_DIR"])
else:
    SOURCE = os.path.join(Path.home(), sys.argv[1])
    DESTINATION = os.path.join(Path.home(), sys.argv[2])
