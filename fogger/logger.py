from datetime import datetime
import os

if os.name == "nt":
    os.system("")


class Fogger:
    RESET = "\033[0m"

    COLORS = {
        "black": "\033[30m",
        "white": "\033[97m",

        "bg_blue": "\033[44m",
        "bg_green": "\033[42m",
        "bg_yellow": "\033[43m",
        "bg_red": "\033[41m",
        "bg_magenta": "\033[45m",
        "bg_white": "\033[47m",
        "bg_cyan": "\033[46m",
    }

    LEVELS = {
        "info": ("bg_blue", "white"),
        "success": ("bg_green", "black"),
        "warning": ("bg_yellow", "black"),
        "error": ("bg_red", "white"),
        "question": ("bg_magenta", "white"),
        "debug": ("bg_cyan", "black"),
    }

    def __init__(
        self,
        format="{time} {badge} {message}",
        badge_style=" {label:^8} "
    ):
        self.format = format
        self.badge_style = badge_style

    def set_format(self, format_string):
        self.format = format_string

    def set_badge_style(self, style):
        self.badge_style = style

    def _time(self):
        return datetime.now().strftime("%H:%M:%S")

    def _build_badge(self, label, bg, fg):
        badge_text = self.badge_style.format(
            label=label.upper()
        )

        return (
            f"{self.COLORS[bg]}"
            f"{self.COLORS[fg]}"
            f"{badge_text}"
            f"{self.RESET}"
        )

    def _log(self, level, message):
        bg, fg = self.LEVELS[level]

        badge = self._build_badge(
            level,
            bg,
            fg
        )

        output = self.format.format(
            time=self._time(),
            badge=badge,
            level=level.upper(),
            message=message
        )

        print(output)

    def info(self, message):
        self._log("info", message)

    def success(self, message):
        self._log("success", message)

    def warning(self, message):
        self._log("warning", message)

    def error(self, message):
        self._log("error", message)

    def question(self, message):
        self._log("question", message)

    def debug(self, message):
        self._log("debug", message)

    def line(self, char="─", length=50):
        print(char * length)

    def space(self):
        print()


# default instance
log = Fogger()