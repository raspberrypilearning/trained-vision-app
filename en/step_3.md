## Collect your training data

Now that you have your your classes set up, you need to add some data to train them with. Each class has two options under 'Add Image Samples': 'Webcam' and 'Upload'. If you had a large collection on photographs of people making the 'rock', 'paper', and 'scissors' gestures on your computer you could upload them. However, as you probably don't have that, you're going to use the 'Webcam' option to record some images now.

--- task ---

Click on the 'Webcam' button for the 'rock' class.

--- /task ---

You will see the class expand to show a preview from your computer's camera (you may need to grant the teachable machine website permission to access your camera) and a 'Hold to Record' button.

![](images/tm_webcam_images.png)

--- task ---

While holding down the 'Hold to Record' button with one hand, make the 'rock' gesture with the other, ensuring that it appears in the preview. Move your hand around and change the shape of the gesture, to ensure there is some variety in the training data.

If you stop recording, don't worry, you can start again by holding down the 'Hold to Record' button. Any new images will just be added to the existing ones.

You should see your images appear in the 'Add Image Samples' section on the right. Keep recording until you have at least 100 of them. More images will usually improve the quality of the model you create, so recording several hundred is a good idea, if you have time.

--- /task ---

If you want to be very thourough in making sure your training data is varied, consider:

  + Switching hands
  + Having other people record themselves making the gesture — but make sure to have them record all three gestures, or the model may learn to associate them with only one!
  + Changing your facial expression
  + Moving so you have a different background

These are all suggestions to avoid the model learning the wrong rules. For example, if there's someone in the background of your 'rock' images who has left by the time you are recording 'paper', it may learn to associate that person with the 'rock' symbol. Or, since you're only recording for a few seconds, it may learn to use the expression on your face. So a good idea might be not to record all of the images for any class all at once, but rather to do some 'rock', then some 'paper' and 'scissors', then back to 'rock' and so on. Can you think of anything else you should consider?

--- task ---

In the same way as you did for 'rock', record training images for 'paper' and 'scissors' using the appropriate gestures.

--- /task ---