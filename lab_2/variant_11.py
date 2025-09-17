class Projector:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(f"{self.name}: Включается")

    def off(self):
        print(f"{self.name}: Выключается")

    def wide_screen_mode(self):
        print(f"{self.name}: Переключение в широкоэкранный режим")

    def tv_mode(self):
        print(f"{self.name}: Переключение в режим ТВ")


class SoundSystem:
    def __init__(self, name):
        self.name = name
        self.volume = 0

    def on(self):
        print(f"{self.name}: Включается")

    def off(self):
        print(f"{self.name}: Выключается")

    def set_volume(self, volume):
        self.volume = volume
        print(f"{self.name}: Уровень громкости установлен на {volume}")

    def surrond_sound(self):
        print(f"{self.name}: Включен объемный звук")

    def stereo_sound(self):
        print(f"{self.name}: Включен стерео звук")


class DVDPlayer:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(f"{self.name}: Включается")

    def off(self):
        print(f"{self.name}: Выключается")

    def play(self, movie):
        print(f"{self.name}: Начинается воспроизведение фильма '{movie}")

    def stop(self):
        print(f"{self.name}: Воспроизведение остановлено")

    def eject(self):
        print(f"{self.name}: Диск извлечен")


class HomeTheaterFacade:
    def __init__(self, projector, sound_system, dvd_player):
        self.dvd = None
        self.projector = projector
        self.sound_system = sound_system
        self.dvd_player = dvd_player

    def watch_movie(self, movie):
        print("Подготовка к просмотру фильма...")
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound_system.surround_sound()
        self.sound_system.set_volume(50)
        self.dvd_player.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Выключение системы домашнего кинотеатра...")
        self.projector.off()
        self.sound_system.off()
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.dvd.player.off()


if __name__ == "__main__":
    projector = Projector("Проектор Epson")
    sound_system = SoundSystem("Акустика Sony")
    dvd_player = DVDPlayer("DVD-проигрыватель Panasonic")
    home_theater = HomeTheaterFacade(projector, sound_system, dvd_player)
    home_theater.watch_movie("Звездные войны")
    home_theater.end_movie()
