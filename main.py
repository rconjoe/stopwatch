from textual.app import App
from textual.widgets import (
    Header,
    Footer,
    Button,
)


class StopwatchApp(App):
    def compose(self):
        yield Header(show_clock=True)
        yield Button("Start")
        yield Button("Stop")
        yield Footer()


if __name__ == "__main__":
    StopwatchApp().run()
