import pygame

class Fala:

    def __init__(self, audio, channel, volume):
        self.audio = pygame.mixer.Sound(audio)
        self.mixer = pygame.mixer.Channel(channel)
        self.mixer.set_volume(volume)


    def play(self):
        self.mixer.play(self.audio)

    def tocando(self):
        return self.mixer.get_busy()

    def stop(self):
        self.mixer.stop()

