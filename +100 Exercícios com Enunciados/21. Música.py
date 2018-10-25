# 21. Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import mp3play
filename = r'/home/rafael/Música/Mau.mp3'
clip = mp3play.load(filename)
clip.play()
