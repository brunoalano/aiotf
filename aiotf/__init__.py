from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __author__, __author_email__, __license__
from .__version__ import __copyright__

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
  from logging import NullHandler
except ImportError:
  class NullHandler(logging.Handler):
    def emit(self, record):
      pass

from .client import AsyncTensorflowServing

__all__ = ['AsyncTensorflowServing']

logging.getLogger(__name__).addHandler(NullHandler())