import os
import sys
from shutil import which


def use_ffmpeg():
    try:
        # try importing
        import ffmpeg

        if which("ffmpeg") is None:
            raise ModuleNotFoundError

    except ModuleNotFoundError as error:
        print("[screener] FFMPEG Not Installed...")

        install_flag = input(
            "[screener] Continue with installing ffmpeg-python?[y/n]: ")

        if install_flag.strip()[0].lower() == "n":
            print("[screener] Skipping FFMPEG...")
            return False

        print("[screener] Installing ffmpeg-python....")

        if sys.platform == 'darwin':
            os.system("HOMEBREW_NO_AUTO_UPDATE=1 brew install ffmpeg")
        elif sys.platform == 'linux':
            os.system("sudo apt install ffmpeg")
        else:
            print("[screener] This OS not supported for FFMPEG System...")
            print("[screener] Skipping FFMPEG...")
            return False
        os.system("pip install ffmpeg")

    except ImportError as error:
        print("[screener] FFMPEG Import Failed, either",
              "change backend or reinstall it properly...")
        return False

    if which("ffmpeg") is not None:
        print("[screener] Installation Failed...")
        print("[screener] Skipping FFMPEG...")
        return False

    # try again for confirmation
    try:
        import ffmpeg
    except:
        print("[screener] FFMPEG Import Failed, either",
              "change backend or reinstall it properly...")
        return False

    print("[screener] Using FFMPEG Backend...")
    return True


def use_pyautogui():
    try:
        import pyautogui

    except ModuleNotFoundError as error:
        print("[screener] PyAutoGui Not Installed...")

        install_flag = input(
            "[screener] Continue with installing pyautogui?[y/n]: ")

        if install_flag.strip()[0].lower() == "n":
            print("[screener] Skipping PyAutoGui...")
            return False
        os.system("pip install pyautogui")

    except ImportError as error:
        print("[screener] PyAutoGui Import Failed, either",
              "change backend or reinstall it properly...")
        return False

    # try again for confirmation
    try:
        import pyautogui
    except:
        print("[screener] PyAutoGui Import Failed, either",
              "change backend or reinstall it properly...")
        return False

    print("[screener] Using PyAutoGui Backend...")
    return True


def auto_select():
    try:
        import ffmpeg
        print("[screener] Using FFMPEG Backend...")
        return True
    except ImportError:
        try:
            import pyautogui
            print("[screener] Using PyAutoGui Backend...")
            return True
        except ImportError:
            return False
    return False


def main():
    if not auto_select() and not use_ffmpeg() and not use_pyautogui():
        print("[screener] Screener Not Supported for your Preferences/System.")
        print("[screener] Please Install either FFMPEG",
              "or PyAutoGui, and try again.")


if __name__ == "__main__":
    main()
