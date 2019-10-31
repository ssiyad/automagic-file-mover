import logging
from pathlib import Path

import os
import argparse

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

DEFAULT = {"SOURCE_DIR": "Downloads", "DESTINATION_DIR": "Moover"}

LOGGER = logging.getLogger(__name__)

# else:
#     SOURCE = os.path.join(Path.home(), sys.argv[1])
#     DESTINATION = os.path.join(Path.home(), sys.argv[2])

arguments = argparse.ArgumentParser()
arguments.add_argument("-s", "--source",
                       help="Source directory")
arguments.add_argument("-d", "--destination",
                       help="Destination directory")
args = arguments.parse_args()

SOURCE = os.path.join(Path.home(), DEFAULT["SOURCE_DIR"])
DESTINATION = os.path.join(Path.home(), DEFAULT["DESTINATION_DIR"])

if args.source:
    SOURCE = os.path.join(Path.home(), args.source)
if args.destination:
    DESTINATION = os.path.join(Path.home(), args.destination)

LOGGER.info("Using SOURCE:{} and DESTINATION:{}".format(SOURCE, DESTINATION))