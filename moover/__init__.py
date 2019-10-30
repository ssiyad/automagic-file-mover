from pathlib import Path
import logging
from . import *

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
path = str(Path.home()) + "/MooverTestDir"
