from clv.logger import logging
from clv.exception import clvException
import sys

try:
    a = 1 / "10"
except Exception as e:
    logging.info(e)
    raise clvException(e, sys) from e

