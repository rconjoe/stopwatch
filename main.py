from textual.app import App
from textual.containers import ScrollableContainer
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
        yield Button("Start", variant="success", id="start")
        yield Button("Stop", variant="error", id="stop")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    CSS_PATH = "main.css"

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        with ScrollableContainer(id="stopwatches"):
            yield Stopwatch()
            yield Stopwatch()
            yield Stopwatch()

    def action_toggle_dark_mode(self):
        self.dark = not self.dark


if __name__ == "__main__":
    StopwatchApp().run()
