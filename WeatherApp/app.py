import eel
from config import Getter


@eel.expose
def collect_data(city: str) -> str:
    getter = Getter()
    return getter.get_data(city)


class Application:
    def __init__(self) -> None:
        eel.init('web')

    @staticmethod
    def run() -> None:
        eel.start('index.html', size=(300, 300), mode='edge')