from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
app = QApplication([])
import pygame,sys

pygame.init()
musica=pygame.mixer.music.load("nose.wav")
pygame.mixer.music.play(1000)


click = 0


def clikeador_de_co0kies():
    global click
    pygame.mixer.music.load("cookie.wav")
    pygame.mixer.music.play()
    click += 1
    print(click)

def juego():
    for_cliker= "cliker"
    data = "cliker: "
    but_cliker= QPushButton(for_cliker)
    v_line.addWidget(but_cliker)
    but_cliker.clicked.connect(clikeador_de_co0kies)
    
def faded():
    pygame.mixer.music.load("nose.wav")
    pygame.mixer.music.play(1000)

def darkside():
    pygame.mixer.music.load("darkside.wav")
    pygame.mixer.music.play(1000)

def the_spectre():
    pygame.mixer.music.load("thespectre.wav")
    pygame.mixer.music.play(1000)

def ajustes():
    for_music= "faded"
    but_music= QPushButton(for_music)
    v_line.addWidget(but_music)
    but_music.clicked.connect(faded)
    for_music2= "darkside"
    but_music2= QPushButton(for_music2)
    v_line.addWidget(but_music2)
    but_music2.clicked.connect(darkside)
    for_music3= "the spectre"
    but_music3= QPushButton(for_music3)
    v_line.addWidget(but_music3)
    but_music3.clicked.connect(the_spectre)

def music():
    for_faded= "faded"
    but_faded= QPushButton(for_faded)
    v_line.addWidget(but_faded)    


def salir():
    blue_label.close()


opcion_1 = "Juego"
opcion_2 = "Ajustes"
opcion_3 = "salir"


but = QPushButton(opcion_1)
but2 = QPushButton(opcion_2)
but3 = QPushButton(opcion_3)
blue_label = QWidget()

blue_label.setWindowTitle('porple_label')
blue_label.move(900, 70)
blue_label.resize(640, 480)


v_line = QVBoxLayout()
v_line.addWidget(but)
v_line.addWidget(but2)
v_line.addWidget(but3)

blue_label.setLayout(v_line)

but.clicked.connect(juego)

but2.clicked.connect(ajustes)

but3.clicked.connect(salir)

blue_label.show()
app.exec_()