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
import pyautogui
import cv2
import numpy as np


class Screener:
    """Object to capture screen of your device.
    """
    def __init__(self, resolution: tuple = (1280, 720), use_pil=True) -> None:
        """Inits Screener class with given resolution & img type.

        Args:
            resolution (tuple, optional): Resolution of catpured image. Defaults to (1280, 720).
            use_pil (bool, optional): Set returned Image type to PIL if True,
                                    else set to ndarray. Defaults to True.
        """
        self._width, self._height = resolution
        self._pil = use_pil

    def capture(self):
        """Catpure screenshot of your device.

        Captures screenshot of device in PIL format,
        and converts image to OpenCV/Ndarray format
        depending on the pil flag specified in initialization.

        Returns:
            screenshot: screenshot of the device screen
        """
        screenshot = pyautogui.screenshot()

        if not self._pil:
            screenshot_np = np.array(screenshot)
            screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)
            return screenshot_np

        else:
            return screenshot
