import logging
from pathlib import Path

import os
import argparse

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename=os.path.join(Path.home(), ".moover_log")
)

DEFAULT = {"SOURCE_DIR": "Downloads", "DESTINATION_DIR": "Moover"}
EXISTING = False

LOGGER = logging.getLogger(__name__)


arguments = argparse.ArgumentParser()
arguments.add_argument("-s", "--source",
                       help="Source directory")
arguments.add_argument("-d", "--destination",
                       help="Destination directory")
arguments.add_argument("-e", "--existing",
                       action="store_true",
                       help="Arrange existing files in source directory")
args = arguments.parse_args()

SOURCE = os.path.join(Path.home(), DEFAULT["SOURCE_DIR"])
DESTINATION = os.path.join(Path.home(), DEFAULT["DESTINATION_DIR"])

if args.source:
    SOURCE = os.path.join(Path.home(), args.source)
if args.destination:
    DESTINATION = os.path.join(Path.home(), args.destination)
if args.existing:
    EXISTING = True
