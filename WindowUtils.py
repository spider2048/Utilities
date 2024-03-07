import win32gui
import win32con
import time

class WindowUtils:
    @staticmethod
    def _enum_windows_callback(hwnd, dst: dict):
        _title = win32gui.GetWindowText(hwnd)
        if dst[0] in _title.lower() and win32gui.IsWindowVisible(hwnd):
            dst[hwnd] = _title

    @staticmethod
    def _enum_child_windows_callback(hwnd, dst: dict):
        dst[hwnd] = win32gui.GetWindowText(hwnd)

    @staticmethod
    def find_window(title):
        found_windows = {0: title.lower()} # hwnd -> title
        win32gui.EnumWindows(WindowUtils._enum_windows_callback, found_windows)
        del found_windows[0]
        return found_windows

    @staticmethod
    def find_window_children(hwnd):
        ret = {}
        win32gui.EnumChildWindows(hwnd, WindowUtils._enum_child_windows_callback, ret)
        return ret

    @staticmethod
    def set_foreground(hwnd):
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.5)

    @staticmethod
    def get_dimensions(hwnd):
        return win32gui.GetWindowRect(hwnd)

    @staticmethod
    def get_next_window(hwnd):
        return win32gui.GetWindow(hwnd, win32con.GW_HWNDNEXT)
