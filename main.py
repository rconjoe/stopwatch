from textual.app import App
from textual.widgets import (
    Header,
    Footer,
    Button,
)


class StopwatchApp(App):
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle dark mode"),
    ]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

    def action_toggle_dark_mode(self):
        self.dark = not self.dark


if __name__ == "__main__":
    StopwatchApp().run()
