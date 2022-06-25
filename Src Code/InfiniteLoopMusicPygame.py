import threading
import pygame
pygame.mixer.init();
pygame.mixer_music.load("C:\Temp\MRisingMusic.mp3");
pygame.mixer_music.play(-1);
x = threading.Event();
x.wait();
