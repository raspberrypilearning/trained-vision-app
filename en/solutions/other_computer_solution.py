import cv2
import tensorflow as tf
import numpy as np
from guizero import App, Box, Text, PushButton
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

model = tf.keras.models.load_model('keras_model.h5', compile=False)


def get_player_throw():
    image = tf.keras.preprocessing.image.load_img(IMG_NAME, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)

    prediction_result = model.predict(image)

    best_prediction = THROWS[np.argmax(prediction_result[0])]

    return best_prediction


def capture_image(image_file_name, brightness = 60):
    cam = cv2.VideoCapture(0)

    tmp, frame = cam.read()

    res = cv2.convertScaleAbs(frame, alpha = 1, beta = brightness)

    cv2.imwrite(image_file_name, res)

    cam.release()


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

    button.text = 'Play again!'


app = App(title='Rock Paper Scissors')

content_box = Box(app, width='fill', align='top')
message = Text(content_box, text="Ready to play?")

button_box = Box(app, width='fill', align='bottom')

# Wire the button to our play_game function
button = PushButton(button_box, text='Play!', command=play_game)

app.display()
