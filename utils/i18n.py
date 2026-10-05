from pathlib import Path
import json

class I18n:
    def __init__(self, locales_dir):
        self.__locales_dir = locales_dir
        self.__translations = {}
        self.__init_localization()

    def __init_localization(self):
        path = Path(self.__locales_dir)
        files = path.glob("*.json")

        for file in files:
            locale = file.stem
            with open (file, encoding='utf-8') as file:
                self.__translations[locale] = json.load(file)

    def get(self, locale, key):
        value = self.__translations[locale]
        for path in key.split('.'):
            if isinstance(value[path], str):
                return value[path]
            value = value[path]

i18n = I18n("./locales")
