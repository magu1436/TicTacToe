
from yaml import safe_load


__config_file_path = "config.yaml"

TITLE_TEXT: str = "三目並べゲーム"
NEW_GAME_BUTTON_TEXT: str = "あたらしいゲーム！"
TO_HOME_BUTTON: str = "ホーム画面へ"

CIRCLE_IMAGE_PATH = "images/maru.png"
CROSS_IMAGE_PATH = "images/batsu.png"


def load_config() -> None:
    """定数を再読込するメソッド"""
    global CIRCLE_IMAGE_PATH
    global CROSS_IMAGE_PATH
    
    config = safe_load(__config_file_path)

    CIRCLE_IMAGE_PATH = config["CIRCLE_IMAGE_PATH"]
    CROSS_IMAGE_PATH = config["CROSS_IMAGE_PATH"]