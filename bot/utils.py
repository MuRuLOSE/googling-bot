import os
from pathlib import Path
import yaml
from aiogram.types import User

BASE_DIR = (
    "/data"
    if "DOCKER" in os.environ
    else os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
) 
BASE_PATH = Path(BASE_DIR)

PATH = f"{BASE_PATH}/bot/"

def get_lang_strings(lang) -> dict:
    if lang == "ru":
        lang_path = PATH + 'langpacks/ru.yaml'

    elif lang == "en":
        lang_path = PATH + 'langpacks/en.yaml'

    with open(lang_path, 'r', encoding='utf-8') as f:
        strings = yaml.safe_load(f)

    return strings

def get_lang(user: User) -> str:
    return user.language_code
