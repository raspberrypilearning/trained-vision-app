import time

import picamera
import tensorflow as tf
import numpy as np
from guizero import App, Box, Text, PushButton, Picture
from random import choice

IMG_NAME = 'throw.jpg'

IMAGE_SIZE = 224

THROWS = ['rock', 'paper', 'scissors']

LOSSES = [
    {'player': 'rock', 'computer': 'paper'},
    {'player': 'paper', 'computer': 'scissors'},
    {'player': 'scissors', 'computer': 'rock'}
]

TIES = [
    {'player': 'rock', 'computer': 'rock'},
    {'player': 'paper', 'computer': 'paper'},
    {'player': 'scissors', 'computer': 'scissors'}
]


def get_player_throw():
    return 'rock'


def capture_image(image_file_name):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        time.sleep(2)
        camera.capture(image_file_name)

def play_game():
    capture_image(IMG_NAME)
    game = {
        'player': get_player_throw(),
        'computer': choice(THROWS)
    }

    if game in LOSSES:
        outcome = 'Better luck next time!'
    elif game in TIES:
        outcome = "It's a tie!"
    else:
        outcome = 'You win!'

    end_game_message = 'You picked {} and the computer picked {}. {}'.format(game['player'],
                                                                             game['computer'],
                                                                             outcome
                                                                             )

    message.value = end_game_message
    throw.image = IMG_NAME
    button.text = 'Play again!'


app = App(title='Rock Paper Scissors')

content_box = Box(app, width='fill', align='top')
message = Text(content_box, text="Ready to play?")
throw = Picture(content_box, image='throw.jpg')
button_box = Box(app, width='fill', align='bottom')

# Wire the button to our play_game function
button = PushButton(button_box, text='Play!', command=play_game)

app.display()