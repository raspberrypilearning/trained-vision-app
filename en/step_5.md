## Make your application

The application you create as part of this project uses the model you have trained to classify an image that is either contained in a file stored on your computer, or captured from your computer's webcam. You need to download your model from Teachable Machine (see 'Export your model' in the previous step) before you can complete the creation of your application.

--- collapse ---
---
title: Create a Python program on your computer
---

Open your programmer's text editor, create a  new file, and save it somewhere on your computer with a name that ends in `.py`. For example,  `project.py`.

**Remember the path to the location of your saved program. You need it to run the program later!**
--- /collapse ---

--- collapse ---
---
title: Run a Python program from the command line
---
You can use the same command line interface (CLI) you used to install the software earlier to run a Python program with the `cd` command to navigate to the directory of your program. Run it with the `python` command on Windows or the `python3` command on macOS or Linux, like so:

```bash
python project.py
```

You should replace `project.py` with whatever you call the file that your program is written in.
--- /collapse ---

--- collapse ---
---
title: Include library code in your program
---
Libraries are collections of code written by other programmers that have been packaged so you can easily install them and then include them in your own programs. Several libraries you might find useful for this project were installed when you ran the setup script.

To use library code, you need to import it into your program, using import statements, like this:
```python
import tensorflow as tf
```
You can use extra keywords, like `as`, to rename a library with a longer name. This means you don’t have to type it each time.

Usually, programmers try to put all of their imports at the start of their program, and keep all imports from the same library on the same line, separated by commas.

--- /collapse ---

### Get an image from your users

--- collapse ---
---
title: Capture an image from the user's camera — Raspberry Pi
---
You can use this function to capture an image using the `picamera` library. You may need to [set up the camera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) before you can use it like this. You also need to decide where on your computer you want to store the image the camera records, so you can provide it to the classifier later. It makes sense to create a variable with that file path and pass it to both this function, and the image classification function.

```python
import time
import picamera

def capture_image(image_file_path):
    with picamera.PiCamera() as camera:
        # Set the size of the image to capture
        camera.resolution = (1024, 768)
        # Wait for two seconds, so the user has a chance to pose/hold up an object/etc.
        time.sleep(2)
        # Capture the image to the file location
        camera.capture(image_file_path)
```

 + `image_file_path` is the path to where you want to store the captured image on your computer. This can be a relative path, like `captured_image.jpg`, or an absolute path, like `/Users/raspberry/projects/machine_vision/captured_image.jpg`.

--- /collapse ---

--- collapse ---
---
title: Capture an image from the user's camera — other computers
---
You can use this function to capture an image using the `cv2` library. You need to decide where on your computer you want to store the image the camera records, so you can provide it to the classifier later. It makes sense to create a variable with that file path and pass it to both this function, and the image classification function.

```python
import cv2

def capture_image(image_file_path):
    # Create a camera object to use to capture images
    cam = cv2.VideoCapture(0)
    # Capture an image from the camera
    frame = cam.read()[1]
    # Adjust the image to be suitably coloured
    # if you find the images are too dark, or bright, try changing beta
    result = cv2.convertScaleAbs(frame, alpha = 1, beta = 60)
    # Turn the result image into a file at image_file_path
    cv2.imwrite(image_file_path, result)
    # Get rid of the camera object
    cam.release()
```

 + `image_file_path` is the path to where you want to store the captured image on your computer. This can be a relative path, like `captured_image.jpg`, or an absolute path, like `/Users/raspberry/projects/machine_vision/captured_image.jpg`. Note that on Windows, file paths use backslashes (`\`) instead of forward slashes (`/`) as separators.

--- /collapse ---

--- collapse ---
---
title: Ask the user for a file path
---
You can directly ask the user for a file path to an image using the built-in `input` function in Python.

```python
image_file_path = input("Where is your image file located?")
```

--- /collapse ---

### Classify an image with your model

--- collapse ---
---
title: Loading the model
---

Move the model you created into the same directory as your Python program. Then you can load it into your program with this code:

```python
import tensorflow as tf
model = tf.keras.models.load_model(model_name, compile=False)
```
 + `model_name` is the full name of the model file. It will probably look something like `keras_model.h5`.

--- /collapse ---

--- collapse ---
---
title: Classify an image file
---

The classifier model takes an image file and returns an array of numbers. The size of the array is the same as the number of classes in your model, and the order of the array matches the order of the classes in Teachable Machine, from top to bottom. So you need to create a list with the names of those classes, to let you display the result in a way your user can understand.

```python
import tensorflow as tf
import numpy as np

# A list of the classes from the Teachable Machine model, in the same order they appear there
CLASSES = ['cat', 'dog', 'fish', 'frog']

# The model expects an image that is a 224x224 pixel square
# Just storing that number to use later
IMAGE_SIZE = 224

def get_image_class(image_file_path):
    # Load the image and resize it
    image = tf.keras.preprocessing.image.load_img(image_file_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
    # Convert the image to an array of numbers
    image = tf.keras.preprocessing.image.img_to_array(image)
    # Expand the array to the shape the model expects
    image = np.expand_dims(image, axis=0)
    # Get a list of the model's prediction of how likely the image is to be each of the classes
    prediction_result = model.predict(image)
    # Get the position in the list of the most likely class
    best_prediction = np.argmax(prediction_result[0])
    # Look up the class name that appears in the same position in the CLASSES list
    best_prediction_name = CLASSES[best_prediction]
    return best_prediction_name
```
--- /collapse ---

--- collapse ---
---
title: Output the classification result
---

Once you have the result, you can just use `print` to output it to your user.

```python
result = get_image_class(image_file_path)

print(f"Your image looks like a {result}.")

```
--- /collapse ---
