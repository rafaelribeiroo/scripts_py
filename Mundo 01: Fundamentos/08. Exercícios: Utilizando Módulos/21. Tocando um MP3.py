# 21. Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame

# Inicializando biblioteca
pygame.init()
# Carregando a música
pygame.mixer.music.load('~/Música/python.mp3')
# Play
pygame.mixer.music.play()
# Aguarde um evento do usuário
pygame.event.wait()
