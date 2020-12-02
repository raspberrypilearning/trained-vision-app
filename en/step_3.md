## Collect your training data

Now that you have your classes set up, you need to add some data to use to train them. Each class has two options under 'Add Image Samples': **Webcam** and **Upload**. If you had a large collection of photographs of people making the 'rock', 'paper', and 'scissors' gestures on your computer, you could upload them. However, as you probably don't have that, you're going to use the **Webcam** option to record some images now. If you are using a Raspberry Pi with a camera, once you have [set up the camera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) it will function as a webcam.

Click on the **Webcam** button for the 'rock' class.

--- /task ---

You will see the class expand to show a preview from your computer's camera (you may need to grant the Teachable Machine website permission to access your camera) and a **Hold to Record** button.

!['rock' class has been expanded. On the left-hand size is the webcam section and Hold to Record button. On the right-hand side is 'Add image 'samples'.](images/tm_webcam_images.png)

--- task ---

While you hold down the **Hold to Record** button with one hand, make the 'rock' gesture with the other, and make sure that it appears in the preview. Move your hand around and change the shape of the gesture, to ensure there is some variety in the training data.

![](images/training.gif)

If you stop recording, don't worry, just hold down the **Hold to Record** button to start again. Any new images will be added to the existing ones.

You should see your images appear in the 'Add Image Samples' section on the right-hand side. Keep recording until you have at least 300 of them. More images will usually improve the quality of the model you create, so recording several hundred is a good idea, if you have time.

--- /task ---

If you want to be very thorough in making sure your training data is varied, you could:

  + Switch hands.
  + Have other people record themselves making the gesture — but make sure to have them record all three gestures, or the model may learn to associate them with only one!
  + Change your facial expression.
  + Move so you have a different background.
  + Change the level of lighting in the room, or moving between bright and dark areas.

These are all suggestions to avoid the model learning the wrong rules. For example, if there's someone in the background of your 'rock' images who has left by the time you are recording 'paper', it may learn to associate that person with the 'rock' class of images. Or, since you're only recording for a few seconds, it may learn to use the expression on your face. So a good idea might be not to record all of the images for any class all at once, but rather to do some 'rock', then some 'paper', and 'scissors', then back to 'rock' and so on. Can you think of anything else you should consider?

--- task ---

Like you did for 'rock', record training images for 'paper' and 'scissors' using the appropriate gestures.

--- /task ---
