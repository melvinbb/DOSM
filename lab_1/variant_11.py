class SettingsManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._instance.theme = 'light'
            cls._instance.language = 'en'
            cls._instance.config_path = 'config.ini'
        return cls._instance

    def __init__(self, *args, **kwargs):
        pass

    def set_theme(self, theme):
        self, theme = theme
        print(f"Тема изменена на: {theme}")

    def set_language(self, language):
        self.language = language
        print(f"Язык изменен на: {language}")

    def set_config_path(self, path):
        print(f"Путь к файлу конфигурации изменен на: {path}")

    def get_settings(self):
        return {
            'theme': self.theme,
            'language': self.language,
            'config_path': self.config_path,
        }


if __name__ == "__main__":
    setting1 = SettingsManager()
    print("Настройки из settings1:",
          setting1.get_settings())
    setting1.set_theme("dark")
    setting2 = SettingsManager()
    print("Настройки из settings2:",
          setting2.get_settings())
    print("settings1 is settings2:",
          setting1 is setting2)
    setting2.set_language("ru")
    print("Настройки из settings1 после изменения через settings2:",
          setting1.get_settings())
setting1.set_config_path("new_config.cfg")
print("Настройки из settings2 после изменения config_path через settings1:",
      setting2.get_settings())
