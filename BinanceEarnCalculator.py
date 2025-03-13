from screeninfo import get_monitors
import eel

from html_render import *
from setings import *
from main import *

PAGE_LIST = [
    'EarnCalculator',
    'Seting'
]
BROWSER_ARGS=[
    # '--disable-dev-shm-usage', 
    # '--disable-dev-tools',
    # '--disable-extensions',
    # '--disable-translate',
    '--lang=en-US',
    # '--kiosk'
]

set = Settings()

@eel.expose
def Settings(type, param):
    match type:
        case "LoadSettings":
            return set.load_settings()
        case "UpdateSettings":
            set.update_settings(param[0], param[1], param[2])
        case "ClearSettings":
            set.clear_setings()
        case "UpdateAutoConver":
            set.update_convert(param[0])

@eel.expose
def Index(type, param):
    match type:
        case "EarnCalculate":
            return EarnCalculate(set, param)
        case "CopyCalculateResult":
            return CopyCalculateResult(set)

if __name__ == '__main__':
    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height
    x = (screen_width - 500) // 2
    y = (screen_height - 550) // 2
    ninja2_render(PAGE_LIST)
    eel.init("web")
    eel.start("EarnCalculator.html", size = (500, 550), position=(x, y), mode = "chrome", port = 3005, jinja_templates="True", cmdline_args= BROWSER_ARGS)