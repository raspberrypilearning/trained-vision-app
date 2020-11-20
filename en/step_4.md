## Create your model

Now that your data is recorded, it's time to train your model!

--- task ---

Train the model by clicking the 'Train Model' button. That was easy!

![](images/tm_train_model.png)

--- /task ---

The training will take a short time, during which you can watch Teachable Machine count the epochs it's running through. **You need to leave your browser open on the Teachable Machine tab, or the model will stop training.** Once the training is complete, you'll see a preview of the model where you can test it by making gestures at your camera and seeing how likely your model thinks that gesture is to be each of 'rock', 'paper', and 'scissors'. The highest percentage indicates the 'guess' that your game would make if it saw that gesture. 


--- task ---

Spend some time testing your model's preview, to see if it usually predicts the gesture you're making correctly.

--- /task ---

--- task ---

If your model doesn't work as you'd like, there are a few things you can try:

  + Add more data by recording some new pictures for each class, in addition to the ones that you already have
  + Open the 'Advanced' section of the 'Training' section and increase the number of epochs, so the model will train for longer

--- /task ---

Once your model is working well enough — it will never be right all the time, but being right most of the time is pretty good — it's time to export the model so you can use it as part of your game.

--- task ---

Click the 'Export Model' button in the 'Preview' section.

![](images/tm_export_model.png)

In the screen that appears, select the 'Tensorflow' tab and, making sure that 'Model conversion type' is set to 'Keras', click the 'Download my model' button.

![](images/tm_download_model.png)

**Make sure you remember where you save the model, you'll need it in a few minutes!**

--- /task ---

Now that you have your model, you're ready to start building your game with it.