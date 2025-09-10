class SettingsManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SettingsManager, cls).__new__(cls)
            return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.theme = 'light'
            self.language = 'en'
            self.config_path = '/path/to/config.ini'
            self.initialized = True

    def set_theme(self, theme):
        self.theme = theme

    def get_theme(self):
        return self.theme

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

    def set_config_path(self, config_path):
        self.config_path = config_path

    def get_config_path(self):
        return self.config_path


if __name__ == "__main__":
    settings1 = SettingsManager()
    print(f"Начальная тема: {settings1.get_theme()}")
    settings2 = SettingsManager()
    print(f"Один и тот же объект: {settings1 is settings2}")
    settings1.set_theme("dark")
    print(f"Тема после изменения через settings1: {settings1.get_theme()}")
    print(f"Тема через settings2: {settings2.get_theme()}")
    settings2.set_language("ru")
    print(f"Язык после изменения через settings2: {settings2.get_language()}")
    print(f"Язык через settings1: {settings1.get_language()}")
