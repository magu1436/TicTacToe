
from yaml import safe_load


__config_file_path = "config.yaml"

TITLE_TEXT: str = "三目並べゲーム"
NEW_GAME_BUTTON_TEXT: str = "あたらしいゲーム！"
TO_HOME_BUTTON: str = "ホーム画面へ"

GRID_WIDTH: int = 10

CIRCLE_IMAGE_PATH = ""
CROSS_IMAGE_PATH = ""
BACKGROUND_PATH = ""
GRID_PATH = ""


def load_config() -> None:
    """定数を再読込するメソッド"""
    global CIRCLE_IMAGE_PATH
    global CROSS_IMAGE_PATH
    global BACKGROUND_PATH
    global GRID_PATH
    
    config = safe_load(__config_file_path)

    CIRCLE_IMAGE_PATH = config["CIRCLE_IMAGE_PATH"]
    CROSS_IMAGE_PATH = config["CROSS_IMAGE_PATH"]
    BACKGROUND_PATH = config["BACKGROUND_PATH"]
    GRID_PATH = config["GRID_PATH"]


load_config()