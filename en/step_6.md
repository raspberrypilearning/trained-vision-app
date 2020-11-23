# Connect your model to the game

First, find the model you downloaded from Teachable Machine. It should be in a file called `converted_keras.zip`.

--- task ---

Unzip `converted_keras.zip` and open the resulting folder. Copy the `keras_model.h5` file to the project directory that contains the code for the game.

--- /task ---

Note that the `labels.txt` file in the unzipped `converted_keras` directory contains the list of human-readable labels and the node numbers they match to on the model's output layer. For a larger number of categories you would have Python read this file and automatically load them but, as there are only three categories in this model, the labels have already been included in the game code for you, in the list called `THROWS`.

Now that your game code and your model are in the same directory, you can load it into the game.

--- task ---

Find the function `get_player_throw`. On a line above it, add the following:

```python
model = tf.keras.models.load_model('keras_model.h5', compile=False)
```

--- /task ---

This will load your model into the game. Now you need to add a function that uses the model to get players' throws — their choice of 'rock', 'paper', or 'scissors'.

--- task ---

Update the `get_player_throw` function with the following code which will load the image the game has captured, then pass it to the model for a prediction. That prediction is then returned, so it can be used by the game code, instead of the default 'rock' that the game came with!

```python
def get_player_throw():
    image = tf.keras.preprocessing.image.load_img(IMG_NAME, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)

    prediction_result = model.predict(image)

    best_prediction = THROWS[np.argmax(prediction_result[0])]

    return best_prediction
```

--- /task ---

To understand each step in this process, you can review the [Testing your computer's vision project](https://projects.raspberrypi.org/en/projects/testing-vision/), particularly the 'Load your model and image' and 'Use the model to predict an image' steps. In short: 

  * All the lines starting with `image` are working to convert the image to the right format for the model
  * The `prediction_result` line is getting the model's prediction in the form of numbers representing confidence in different guesses
  * The `best_prediction` line is taking the prediction with the highest value (`np.argmax` gets the index of the highest value in a list) and using it to look up the label of that prediction in the THROWS list.

--- save ---

Run the program and play with it a few times! If you're not happy with the quality of its guesses, think about any differences between the training data and the inputs you're giving your game — maybe the light has changed, or you're wearing different clothes, etc. If you need to, you can record more training data in Teachable Machine, train your model again, and then download it and replace the model you're using in the game with an updated version.
