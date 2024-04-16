from textual.app import App
from textual.widgets import (
    Header,
    Footer,
    Button,
    Static,
)


class TimeDisplay(Static):
    pass


class Stopwatch(Static):
    def compose(self):
        yield Button("Start", variant="success")
        yield Button("Stop", variant="error")
        yield Button("Reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    def compose(self):
        yield Header(show_clock=True)
        yield Stopwatch()
        yield Stopwatch()
        yield Stopwatch()
        yield Footer()

    def action_toggle_dark_mode(self):
        self.dark = not self.dark


if __name__ == "__main__":
    StopwatchApp().run()
