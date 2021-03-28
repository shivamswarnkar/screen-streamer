"""Save or Record screen of your device.

Use this module to capture your screen for some duration of time
or to capture frame by frame for dispaly or streaming.

  Typical usage example:

  from screener import Screener
  screener = Screener()

  # record 30 seconds
  screener.record(duration=30)

  # get one ndarray representing BGR image
  frame = screener.capture()
"""

from .screener import Screener
