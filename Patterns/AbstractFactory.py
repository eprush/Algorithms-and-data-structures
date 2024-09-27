from typing import Protocol
from sys import platform
import socket


class TextLabel(Protocol): ...


class Button(Protocol): ...


class Window(Protocol):
    def draw(self): ...

    def add(self, text_label: TextLabel): ...

    def click(self, button: Button): ...


class GUI(Protocol):
    def create_window(self, title: str, width: int, height: int) -> Window: ...

    def create_text_label(self, text: str) -> TextLabel: ...

    def create_button(self, text: str) -> Button: ...


class WindowsGUI:
    def create_window(self, title: str, width: int, height: int) -> Window:
        """Realization of creating new window at Windows"""

    def create_text_label(self, text: str) -> TextLabel:
        """Realization of creating new text label at Windows"""

    def create_button(self, text: str) -> Button:
        """Realization of creating new button at Windows"""


class LinuxGUI:
    def create_window(self, title: str, width: int, height: int) -> Window:
        """Realization of creating new window at Linux"""

    def create_text_label(self, text: str) -> TextLabel:
        """Realization of creating new text label at Linux"""

    def create_button(self, text: str) -> Button:
        """Realization of creating new button at Linux"""


def draw_greetings_screen(username: str, gui: GUI) -> None:
    window = gui.create_window(title="Hi!", width=100, height=100)
    t = gui.create_text_label(f"Dear {username}")
    window.add(t)
    window.draw()
    b = gui.create_button("Continue")
    window.click(b)
    return


def main():
    if platform == "win32":
        gui = WindowsGUI()
    elif platform == "linux":
        gui = LinuxGUI()
    else:
        raise ValueError
    draw_greetings_screen(socket.gethostname(), gui)
